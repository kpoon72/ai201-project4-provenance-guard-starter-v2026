#!/usr/bin/env python3
"""
Criterion 4 (and the rest of criterion 5), three trials.  <- UNIT 8, MILESTONE 3

    python app.py                                  # in one terminal
    python eval_appeals.py --label before          # in another

`run_eval.py` only ever calls /submit, and it always sends a JSON object, so
two things in criteria.md can't be tested through it:

  4. An appeal against a real content_id returns status "under_review" and
     adds an appeal entry for that id to the audit log. An unknown id gets 404.
  5. A body that isn't JSON, or is JSON but not an object, gets a 400.

Each trial submits 5 texts, appeals each one, and reads GET /log back to check
the appeal entry landed. Like run_eval.py, it records what came back and
leaves the verdict to me.
"""

import argparse
import datetime as dt
import json

import requests

import config

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"

TEXTS = [
    "We got to the lake late, so the good spots were taken. We set up near the "
    "parking lot instead and it was fine. My brother burned the hot dogs again.",
    "The library closes at nine on weekdays, which is too early for me. I usually "
    "end up at the coffee shop down the street until they kick me out too.",
    "My first job was washing dishes at a diner. The cook yelled a lot but he "
    "always saved me a plate of fries at the end of the night.",
    "I tried to fix the bike chain myself and made it worse. Took it to the shop "
    "and the guy fixed it in two minutes. He didn't even charge me.",
    "It rained the whole weekend so we stayed in and played cards. My grandma won "
    "every single game and pretended it was luck.",
]

NOT_AN_OBJECT = [
    ("body is not JSON", "this is not json", "application/json"),
    ("body is a JSON array", '["text", "creator_id"]', "application/json"),
]


def run_trial(url, trial, timeout):
    appeals = []
    for i, text in enumerate(TEXTS, 1):
        submit = requests.post(f"{url}/submit", timeout=timeout,
                               json={"text": text, "creator_id": f"eval_appeal_{i}"})
        submitted = submit.json()
        content_id = submitted.get("content_id")

        appeal = requests.post(f"{url}/appeal", timeout=timeout, json={
            "content_id": content_id,
            "reasoning": f"Eval trial {trial}: testing that an appeal is recorded.",
        })
        appealed = appeal.json()

        log = requests.get(f"{url}/log", timeout=timeout).json()["entries"]
        logged = [e for e in log
                  if e.get("content_id") == content_id and e.get("event") == "appeal"]

        appeals.append({
            "content_id": content_id,
            "submit_status": submit.status_code,
            "appeal_status": appeal.status_code,
            "status_returned": appealed.get("status"),
            "appeal_entries_in_log": len(logged),
            "log_entry": logged[-1] if logged else None,
        })

    unknown = requests.post(f"{url}/appeal", timeout=timeout, json={
        "content_id": "00000000-0000-0000-0000-000000000000",
        "reasoning": "This id was never submitted.",
    })

    bad_bodies = []
    for name, raw, content_type in NOT_AN_OBJECT:
        r = requests.post(f"{url}/submit", data=raw, timeout=timeout,
                          headers={"Content-Type": content_type})
        bad_bodies.append({"sent": name, "status": r.status_code,
                           "response": r.json() if r.content else None})

    return {
        "appeals": appeals,
        "unknown_id": {"status": unknown.status_code, "response": unknown.json()},
        "not_an_object": bad_bodies,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--timeout", type=float, default=90.0)
    args = parser.parse_args()

    trials = []
    for trial in range(1, args.trials + 1):
        result = run_trial(args.url, trial, args.timeout)
        trials.append(result)
        ok = sum(a["status_returned"] == "under_review" and a["appeal_entries_in_log"] > 0
                 for a in result["appeals"])
        bad = ", ".join(str(b["status"]) for b in result["not_an_object"])
        print(f"trial {trial}: appeals recorded {ok}/{len(result['appeals'])}, "
              f"unknown id -> {result['unknown_id']['status']}, not-an-object -> {bad}")

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"appeals_{stamp}{label}.md"
    lines = [
        f"# Appeals and non-object bodies{f' — {args.label}' if args.label else ''}",
        "",
        "- Produced by: `eval_appeals.py::main`",
        "- Service: `app.py::appeal`, `app.py::submit`",
        f"- {args.trials} trials · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
    ]
    for n, result in enumerate(trials, 1):
        lines += [f"## Trial {n}", "", "```json", json.dumps(result, indent=2, ensure_ascii=False),
                  "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()

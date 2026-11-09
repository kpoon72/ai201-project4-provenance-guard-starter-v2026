# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

Provenance Guard is a small backend a writing site can call. It takes a piece
of writing and returns a guess about whether AI wrote it, how confident that
guess is, a plain-English label for the reader, and a way for the writer to
appeal.

1. **`POST /submit` receives the text** with a `creator_id` (`app.py::submit`).
2. **The input is checked.** Missing, empty, too-short or too-long text gets a
   400 with a reason, and the rejection is logged.
3. **A `content_id` is minted** (uuid4). It's the handle for appeals and ties
   the log entries together.
4. **Signal one scores predictability** (`detector.py::model_signal`).
5. **Signal two scores the shape of the text** (`stylometry.py::style_signal`).
6. **The two scores are combined and labeled** (`scoring.py::combine_signals`
   and `scoring.py::score_to_label`).
7. **The decision is logged and returned** (`audit.py::log_decision` writes to
   `logs/audit.jsonl`). The reader sees the label. If the writer disagrees,
   `POST /appeal` moves the item to `under_review`.

Full design notes, including the false-positive walk-through and the endpoint
contracts: [design.md](design.md).


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to gpt2 (perplexity), turned
into a 0–1 score where higher means more likely AI.

**Why that might differ between human and AI writing:** A language model
writes by picking likely next words, so its output is easy for a model to
predict. People make odd, specific word choices a model wouldn't guess.

**What it can't see:** Who wrote it. It rewards plainness, not machine
authorship, so second-language writers, younger writers and anyone writing
simply score as machine-like. AI text pushed toward rare words can score as
human. It only reads the first ~400 tokens.

### Signal two — the style signal

**What it measures:** The shape of the text without reading it: spread of
sentence lengths, vocabulary variety and punctuation use, combined into a 0–1
score where higher means more likely AI.

**Why that might differ between human and AI writing:** Generated prose tends
toward even, mid-length sentences, a narrower vocabulary and tidy punctuation.
Human writing is lumpier.

**What it can't see:** Meaning. Typos, broken-up sentences, pasted quotations
or lists change the shape without changing who wrote it. It's unstable on very
short text.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**How signal two is built** (`stylometry.py::style_signal`): three measures,
each mapped linearly onto 0–1 between a "human" anchor and an "AI" anchor,
clipped, then averaged equally. A measure that can't be computed (one
sentence, no words) is left out; if none can be, the signal is 0.5.

| Measure | What it computes | Direction | Human anchor → AI anchor |
|---|---|---|---|
| Sentence-length spread | stdev / mean of words per sentence | low = AI | 0.8 → 0.1 |
| Word variety | unique / total words, averaged over 50-word windows | high = AI | 0.70 → 0.95 |
| Punctuation density | commas, semicolons, dashes, quotes, ! ? etc. per 10 words | high = AI | 0.2 → 1.0 |

The directions for word variety and punctuation came from the calibration run
below, not from a guess. I expected varied vocabulary to mean human, but the
AI text had the *most* varied words (0.95) and the most commas (0.91), and
plain human writing had the least. Flipping them also helps the writer signal
one is most likely to accuse, because plain writing scores *human* on both.

**The rule:** Average the two signals equally. If they differ by 0.4 or more,
they disagree, and disagreement means unsure: the combined score is capped at
0.64, just below the AI line, so a split can never produce an accusation.

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.5`, `WEIGHT_STYLE_SIGNAL = 0.5`,
`DISAGREEMENT_GAP = 0.4`, `DISAGREEMENT_CAP = 0.64`, `HUMAN_THRESHOLD = 0.35`,
`AI_THRESHOLD = 0.65`, all in `config.py`.

**Where it lives:** `scoring.py::combine_signals`

**Calibration run** (four deliberately chosen inputs through `POST /submit`):

| Input | model_score | style_score | combined |
|---|---|---|---|
| Clearly AI (generic essay on AI's benefits and risks) | 0.788 | 0.867 | 0.828 |
| Clearly human (casual note: bus, sleet, grandma's soup) | 0.312 | 0.387 | 0.349 |
| Plain human (short, even sentences about starting to run) | 0.824 | 0.421 | 0.623 |
| Lightly-edited AI (the AI essay reworded casually) | 0.681 | 0.602 | 0.641 |

Clearly AI and clearly human are 0.48 apart. The lightly-edited AI lands in
"unsure", just under the AI line: light editing is enough to get past it.

**A case where my two signals split, and what my rule does with it:** The
plain human paragraph. Signal one says 0.82 (AI), because short common-word
sentences are easy for gpt2 to predict. Signal two says 0.42 (leaning human),
because its vocabulary repeats and it uses almost no punctuation. They differ
by 0.40, so the disagreement rule applies: the combined score can't exceed
0.64, and the writer gets "unsure" rather than an accusation. Here the plain
average (0.62) was already under the cap. The cap matters when the model signal
is higher still.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was written by a person. |
| unsure | 0.35 – 0.65 | We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged. |
| high-confidence AI | 0.65 – 1.00 | Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it. |

A score of exactly 0.35 is human and exactly 0.65 is AI
(`scoring.py::score_to_label`), so every score from 0 to 1 gets one of the
three labels. All three were reached in testing: the calibration "clearly
AI" text scored 0.828 (AI), "clearly human" 0.349 (human), and "plain human"
0.623 (unsure).

**Why I worded the "unsure" one this way:** Many writers who land in "unsure"
wrote every word themselves. Plain human writing is exactly what lands there.
So the label says plainly that no judgment was made and nothing was flagged,
and it doesn't hint at suspicion. The AI label is worded as the system's guess
rather than a fact about the writer, and it always says how to appeal.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

> Run on port 5001 (`PORT=5001 python app.py`): on macOS the AirPlay Receiver
> holds port 5000 and answers every request with a 403.

The submission is a generic AI-style test paragraph, so it gets the AI label.
The appeal is then sent against its `content_id`.

```bash
$ curl -X POST http://127.0.0.1:5001/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Artificial intelligence has transformed many industries in recent years. It offers numerous benefits, including increased efficiency and improved decision-making. However, it also presents significant challenges that must be carefully addressed. Organizations should consider ethical implications, data privacy, and workforce impacts. By adopting a balanced approach, society can harness the potential of artificial intelligence while minimizing its risks. Overall, the future of artificial intelligence looks promising.", "creator_id": "kamal"}'
```

```json
{
  "confidence": 0.8277,
  "content_id": "106c3cd0-e8be-4a44-a311-2891671ea61d",
  "creator_id": "kamal",
  "guess": "ai",
  "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
  "model_score": 0.7881,
  "status": "decided",
  "style_score": 0.8674
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5001/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "106c3cd0-e8be-4a44-a311-2891671ea61d", "reasoning": "I wrote this essay myself for my AI201 class. I used a formal style because it was an assignment."}'
```

```json
{
  "content_id": "106c3cd0-e8be-4a44-a311-2891671ea61d",
  "message": "Thanks \u2014 we've received your appeal. A person will review this decision, and it's marked as under review until they do.",
  "original_guess": "ai",
  "status": "under_review"
}
```

An appeal for an id that doesn't exist is refused instead of failing silently:

```bash
$ curl -X POST http://127.0.0.1:5001/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "not-a-real-id", "reasoning": "test"}'
```

```json
{
  "error": "unknown_content_id",
  "message": "No submission has the id 'not-a-real-id'."
}
```

**What the log shows afterwards**

The two entries for this `content_id`: the original decision, untouched, and
the appeal after it with `status: "under_review"`.

```bash
$ curl "http://127.0.0.1:5001/log?limit=10"
```

```json
{
  "combined_score": 0.8277,
  "content_id": "106c3cd0-e8be-4a44-a311-2891671ea61d",
  "creator_id": "kamal",
  "guess": "ai",
  "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
  "model_score": 0.7881,
  "status": "decided",
  "style_score": 0.8674,
  "timestamp": "2026-10-29T00:47:34+00:00"
},
{
  "content_id": "106c3cd0-e8be-4a44-a311-2891671ea61d",
  "creator_id": "kamal",
  "event": "appeal",
  "reasoning": "I wrote this essay myself for my AI201 class. I used a formal style because it was an assignment.",
  "status": "under_review",
  "timestamp": "2026-10-29T00:47:34+00:00"
}
```

### Earlier checks

Bad input gets a 400 and a rejection entry instead of a crash:

```bash
$ curl -X POST http://127.0.0.1:5001/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "   ", "creator_id": "k"}'
```

```json
{
  "error": "empty_text",
  "message": "\"text\" can't be empty."
}
```

```bash
$ curl "http://127.0.0.1:5001/log?limit=1"
```

```json
{
  "count": 1,
  "entries": [
    {
      "creator_id": "k",
      "event": "rejected",
      "reason": "text_too_long",
      "status": "rejected",
      "timestamp": "2026-10-29T00:41:04+00:00"
    }
  ]
}
```

What one signal says about three texts (`python detector.py "..."`):

| Text | model_signal |
|---|---|
| Generic AI-style paragraph about AI's benefits and challenges | 0.8647 |
| Casual human note with slang and typos ("ok so the bus never came??") | 0.0368 |
| Plain human paragraph about starting to run | 0.8174 |

The plain human paragraph scores almost as AI-like as the AI one. That's the
blind spot named above: signal one rewards plainness, not machine authorship.

*Milestone 3 — one signal, placeholder confidence and label:*

```bash
$ curl -X POST http://127.0.0.1:5001/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I started running last spring because my doctor told me to. The first week was hard and I could barely finish a mile. Now I run three times a week and I feel much better. My knees still hurt sometimes, but I think it is worth it.", "creator_id": "kamal"}'
```

```json
{
  "confidence": 0.8174,
  "content_id": "cb1ff141-eb66-4700-8199-b739cb93b333",
  "creator_id": "kamal",
  "guess": "pending",
  "label": "PLACEHOLDER — label comes in Milestone 5.",
  "model_score": 0.8174,
  "status": "decided",
  "style_score": null
}
```

The log entry it wrote (`logs/audit.jsonl`):

```json
{
  "timestamp": "2026-10-29T00:41:04+00:00",
  "content_id": "cb1ff141-eb66-4700-8199-b739cb93b333",
  "creator_id": "kamal",
  "guess": "pending",
  "model_score": 0.8174,
  "style_score": null,
  "combined_score": 0.8174,
  "label": "PLACEHOLDER — label comes in Milestone 5.",
  "status": "decided"
}
```


---

## How I Used AI

I used Claude Code (Claude Opus 5.5) throughout this project. It wrote most of
the code and drafted the design notes. I made the decisions, reviewed each
milestone and made every commit myself.

**Moment 1 — the acceptance criteria**

- *What I asked for:* Help writing `criteria.md`. I asked Claude to write the
  criteria for me.
- *What came back:* It said the brief doesn't allow a model to write the
  criteria. Instead it asked me to choose a target for each area, with the
  trade-off of each option. After I chose, it pointed out that two of my
  picks (a 0.20 score spread and 1 piece per label) were easy enough that I
  could hardly miss them.
- *What I changed:* I raised the score-spread target from 0.20 to 0.30 and kept
  the rest, including 0 of 10 false positives, even though Claude warned it
  might be hard to meet with gpt2. Claude drafted the "Why this target" reasons
  from my choices. I read them and kept them.

**Moment 2 — the style signal and the combining rule**

- *What I asked for:* Build the style signal and show me options for combining
  the two signals.
- *What came back:* Claude's first assumption, that varied vocabulary means
  human, was wrong on the calibration texts: the AI text had the *most* varied
  words and the most commas. It flipped those two directions and showed me four
  combining rules, with each one's scores on my four test inputs.
- *What I changed:* I rejected the 60/40 model-heavy rule because it labeled
  the plain human paragraph as AI (0.66), which breaks my criterion 1. I chose
  equal weights plus a disagreement cap, so that when the signals split by 0.4
  or more, the writer gets "unsure" instead of an accusation. I also picked the
  wording of all three labels from Claude's drafts, choosing the "no judgment"
  version of the unsure label.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day (`config.py`, applied to `POST /submit`
in `app.py`)

**Why those numbers and not others:** A real writer posts a piece, maybe fixes
a typo and posts again. That's a few submissions in a minute and rarely more
than a handful in a day, so 5 per minute and 50 per day never get in their way.
A script trying to map my thresholds needs hundreds of slightly different
variations. At 5 per minute it can send only one probe every 12 seconds, and
at 50 per day it gets a single small batch, not enough to find where 0.65
sits. I chose the stricter numbers over the starter's 10 and 200 because the
day limit is what really stops slow, patient probing.

**What a caller counts as:** The `creator_id` in the request, falling back to
the caller's IP address when there's no usable `creator_id`
(`app.py::rate_limit_key`). The weakness: a script can make up a new
`creator_id` for every request and never hit the limit, so per-creator limits
only work if creator ids are tied to real accounts. Per address would stop
that, but would also make one household or school network share one limit.

**The run of status codes when I pushed past it:**

```
$ python run_attacks.py --flood 15
15 submissions as 'flood_tester' against http://127.0.0.1:5001

============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================

10 of 15 were rate limited.
Wrote results/flood_2026-11-08_2038.md
```

Each 429 leaves a rejection in the audit log:

```json
{
  "creator_id": "flood_tester",
  "event": "rejected",
  "limit": "5 per 1 minute",
  "reason": "rate_limited",
  "status": "rejected",
  "timestamp": "2026-11-09T02:38:40+00:00"
}
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

`python run_attacks.py --set attack_set --label before`, full report in
`results/attack_run_2026-11-08_2044_before.md`. All 56 inputs ran, with no
crashes and no 500s.

**How I marked them.** An attack BROKE if it got what it was going for:

- **evasion:** AI text that did *not* get the AI label.
- **false_positive:** human text that *did* get the AI label.
- **prompt_injection:** AI text that escaped the AI label, or an
  instruction that changed the label text or the log.
- **malformed:** a crash or 500, or a confident label given to something
  that isn't writing.
- **flood:** submissions from one creator that weren't cut off.

**Totals: 43 held, 13 broke.**

| Family | Held | Broke |
|---|---|---|
| evasion | 2 | 8 |
| false_positive | 8 | 0 |
| prompt_injection | 3 | 3 |
| malformed | 18 | 2 |
| flood_same_creator | 12 | 0 |

| ID | Targeting | Status | Guess | Score | model | style | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | signal two: typos raise word variety | 200 | unsure | 0.425 | 0.164 | 0.687 | BROKE |
| EV02 | signal two: broken-up sentences raise length spread | 200 | unsure | 0.454 | 0.594 | 0.313 | BROKE |
| EV03 | signal two: a pasted quotation changes the shape | 200 | ai | 0.677 | 0.666 | 0.688 | HELD |
| EV04 | signal one: unusual words raise perplexity | 200 | unsure | 0.646 | 0.611 | 0.681 | BROKE |
| EV05 | both signals: heavy human editing pass | 200 | unsure | 0.382 | 0.321 | 0.443 | BROKE |
| EV06 | signal two: one very long sentence and one very short | 200 | unsure | 0.412 | 0.573 | 0.251 | BROKE |
| EV07 | signal two: padding with punctuation | 200 | ai | 0.689 | 0.586 | 0.791 | HELD |
| EV08 | signal one: text below the token window | 200 | unsure | 0.412 | 0.245 | 0.580 | BROKE |
| EV09 | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.639 | 0.704 | 0.575 | BROKE |
| EV10 | signal two: repeated stanza structure | 200 | unsure | 0.586 | 0.979 | 0.193 | BROKE |
| FP01 | plain, clear human writing with no flourishes | 200 | unsure | 0.461 | 0.618 | 0.305 | HELD |
| FP02 | human writing in a formal register | 200 | unsure | 0.549 | 0.739 | 0.359 | HELD |
| FP03 | a non-native English speaker writing carefully | 200 | unsure | 0.595 | 0.805 | 0.384 | HELD |
| FP04 | a student essay written to a rubric | 200 | unsure | 0.600 | 0.833 | 0.368 | HELD |
| FP05 | technical documentation written by a person | 200 | unsure | 0.543 | 0.800 | 0.285 | HELD |
| FP06 | a person imitating a formal template | 200 | unsure | 0.545 | 0.881 | 0.208 | HELD |
| FP07 | human writing that repeats a phrase deliberately | 200 | unsure | 0.486 | 0.882 | 0.091 | HELD |
| FP08 | very short genuine human submission | 200 | unsure | 0.415 | 0.322 | 0.508 | HELD |
| PI01 | instruction to ignore the check | 200 | unsure | 0.419 | 0.463 | 0.377 | BROKE |
| PI02 | instruction disguised as a system message | 200 | unsure | 0.355 | 0.204 | 0.506 | BROKE |
| PI03 | instruction wrapped in the writer's voice | 200 | unsure | 0.627 | 0.594 | 0.659 | BROKE |
| PI04 | attempt to make the label text hostile | 200 | unsure | 0.574 | 0.500 | 0.649 | HELD |
| PI05 | attempt to inject into the audit log | 200 | ai | 0.732 | 0.640 | 0.823 | HELD |
| PI06 | instruction plus real human text | 200 | unsure | 0.439 | 0.558 | 0.319 | HELD |
| MF01 | text is only whitespace | 400 | — | — | — | — | HELD |
| MF02 | text is a single character | 400 | — | — | — | — | HELD |
| MF03 | text is control characters | 200 | human | 0.250 | 0.000 | 0.500 | BROKE |
| MF04 | text is only punctuation | 200 | human | 0.256 | 0.011 | 0.500 | BROKE |
| MF05 | text is a very long single word | 200 | unsure | 0.640 | 0.998 | 0.500 | HELD |
| MF06 | text is emoji only | 200 | unsure | 0.640 | 0.997 | 0.500 | HELD |
| MF07 | text is right-to-left script | 200 | unsure | 0.640 | 0.906 | 0.500 | HELD |
| MF08 | text is 60,000 characters | 400 | — | — | — | — | HELD |
| RQ01–RQ09 | no text, no creator_id, text a number / list / null, creator_id an object, body an array / unparseable / empty | 400 | — | — | — | — | HELD (9) |
| RQ10 | body is form-encoded, not JSON | 429 | — | — | — | — | HELD* |
| RQ11 | body is JSON claiming to be plain text | 429 | — | — | — | — | HELD* |
| RQ12 | deeply nested JSON | 400 | — | — | — | — | HELD |
| FL01_01–05 | 20 rapid submissions from one creator | 200 | human | 0.264 | 0.029 | 0.500 | HELD (5) |
| FL01_06–12 | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD (7) |

\* RQ10 and RQ11 carry no usable `creator_id`, so the limiter counted them
against my IP address, which the RQ rows before them had already used up.
They got a 429 and never reached the route. Sent by hand a minute later,
both got `400 invalid_json`, so the route holds them too.

**Ten audit log entries from the run**

Chosen to show the failures and near misses, plus two rejections.

```json
{"timestamp": "2026-11-09T02:44:44+00:00", "content_id": "47be26aa-0639-47b9-83da-83b94ab3613d", "creator_id": "attacker_EV10", "guess": "unsure", "model_score": 0.9792, "style_score": 0.1934, "combined_score": 0.5863, "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.", "status": "decided"}
{"timestamp": "2026-11-09T02:44:43+00:00", "content_id": "c2616016-f1f8-4d0d-90a4-54120078f124", "creator_id": "attacker_EV01", "guess": "unsure", "model_score": 0.1635, "style_score": 0.6874, "combined_score": 0.4254, "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.", "status": "decided"}
{"timestamp": "2026-11-09T02:44:43+00:00", "content_id": "ca8f2fc2-94b2-49f1-89f5-514116284219", "creator_id": "attacker_EV09", "guess": "unsure", "model_score": 0.7042, "style_score": 0.5745, "combined_score": 0.6394, "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.", "status": "decided"}
{"timestamp": "2026-11-09T02:44:44+00:00", "content_id": "16c5bbb6-c345-468f-a344-5c08f51a4f87", "creator_id": "attacker_PI02", "guess": "unsure", "model_score": 0.2044, "style_score": 0.5057, "combined_score": 0.3551, "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.", "status": "decided"}
{"timestamp": "2026-11-09T02:44:44+00:00", "content_id": "05167f50-07b6-4dd9-9ec4-faf9d20bc228", "creator_id": "attacker_FP04", "guess": "unsure", "model_score": 0.8329, "style_score": 0.3677, "combined_score": 0.6003, "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.", "status": "decided"}
{"timestamp": "2026-11-09T02:44:45+00:00", "content_id": "fec09d56-5933-42ca-8bbe-c6ac8b6195b8", "creator_id": "attacker_MF07", "guess": "unsure", "model_score": 0.9064, "style_score": 0.5, "combined_score": 0.64, "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.", "status": "decided"}
{"timestamp": "2026-11-09T02:44:45+00:00", "content_id": "f6f02f25-4105-4aa3-954a-e6f6f9c798a5", "creator_id": "attacker_MF03", "guess": "human", "model_score": 0.0, "style_score": 0.5, "combined_score": 0.25, "label": "We think this was written by a person.", "status": "decided"}
{"timestamp": "2026-11-09T02:44:45+00:00", "content_id": "258bd8e0-52f7-493a-909a-9b3d2db85d27", "creator_id": "attacker_PI05", "guess": "ai", "model_score": 0.6401, "style_score": 0.8231, "combined_score": 0.7316, "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.", "status": "decided"}
{"timestamp": "2026-11-09T02:44:46+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
{"timestamp": "2026-11-09T02:44:45+00:00", "creator_id": "attacker_RQ05", "event": "rejected", "status": "rejected", "reason": "missing_text"}
```

**The single worst outcome:** MF07, a short paragraph of real writing in
Arabic. Signal two can't see it at all: its word pattern only matches the
letters a–z, so it finds no words and falls back to 0.5. Signal one (gpt2,
trained on English) gave it 0.91. Their plain average is 0.70, an AI label.
The only reason this writer wasn't told their work looks AI-written is the
disagreement cap pulling it down to exactly 0.64, one hundredth under the
line. A writer working in any non-Latin script is one small change away from
being accused, by two signals that can't read their language.


**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing labeled AI | 0 of 10 | 7/10 | 7/10 | 7/10 | MISSED |
| 2. Gap between clearly-AI and clearly-human averages | ≥ 0.30 | 0.099 | 0.099 | 0.099 | MISSED |
| 3. All three labels reached by my test inputs | 3 of 3 | 2/3 | 2/3 | 2/3 | MISSED |
| 4. Valid appeals return under_review and are logged; unknown id gets 404 | 5 of 5, plus 404 | 5/5, 404 | 5/5, 404 | 5/5, 404 | MET |
| 5. Bad input gets a 400 | 11 of 11 | 11/11 | 11/11 | 9/11 | MISSED |

How the trials were run:

- **Criteria 1, 2, 3 and most of 5:** `python run_eval.py --label before`,
  using the scenarios in `scenarios.py`. Report:
  `results/run_2026-11-08_2055_before.md`, produced by `run_eval.py::main`.
- **Criterion 4 and the two bodies that aren't JSON objects:**
  `run_eval.py` only calls `/submit` and always sends a JSON object, so I
  added `eval_appeals.py`. Each trial submits 5 texts, appeals each one, and
  reads `GET /log` back to check the appeal entry landed. It also sends an
  unknown id and the two non-object bodies. Report:
  `results/appeals_2026-11-08_2048_before.md`, produced by
  `eval_appeals.py::main`.

The scores were identical in all three trials, as expected: neither signal is
random. Criterion 5 is the only one that differed, and that came from the
rate limiter, not the scoring.

**Real output from one trial**

*Criterion 1:* one of my own pieces labeled AI. Trial 1, `run_eval.py::main`:

```json
{
  "status": 200,
  "guess": "ai",
  "confidence": 0.8086,
  "model_score": 0.9123,
  "style_score": 0.7049,
  "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
  "sent": "One place I remember very well is Nepal, where I grew up. Even though "
}
```

All ten of my pieces, combined score (model / style), same in every trial:
0.63 (0.79/0.46) unsure, 0.57 (0.82/0.32) unsure, **0.81** (0.91/0.70) AI,
0.62 (0.83/0.41) unsure, **0.80** (0.83/0.78) AI, **0.80** (0.94/0.66) AI,
**0.78** (0.91/0.65) AI, **0.68** (0.83/0.52) AI, **0.79** (0.85/0.73) AI,
**0.77** (0.85/0.68) AI.

*Criterion 2:* one clearly-AI piece. Trial 1, `run_eval.py::main`:

```json
{
  "status": 200,
  "guess": "ai",
  "confidence": 0.8863,
  "model_score": 0.9353,
  "style_score": 0.8373,
  "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
  "sent": "Climate change is one of the most pressing challenges facing the world"
}
```

Clearly-AI average 0.785 (0.82, 0.89, 0.75, 0.73, 0.74). Clearly-human average
0.686 (0.63, 0.57, 0.81, 0.62, 0.80, my first five pieces). Gap 0.099.

*Criterion 3:* labels seen across all 22 text inputs in a trial: `ai` and
`unsure`, never `human`. The lowest score of any input was 0.57. Borderline
set, trial 1: 0.73 AI and 0.63 unsure.

*Criterion 4:* one appeal. Trial 1, `eval_appeals.py::main`:

```json
{
  "content_id": "e97a7731-79ab-42c1-9d84-7ef35fd06929",
  "submit_status": 200,
  "appeal_status": 200,
  "status_returned": "under_review",
  "appeal_entries_in_log": 1,
  "log_entry": {
    "content_id": "e97a7731-79ab-42c1-9d84-7ef35fd06929",
    "creator_id": "eval_appeal_1",
    "event": "appeal",
    "reasoning": "Eval trial 1: testing that an appeal is recorded.",
    "status": "under_review",
    "timestamp": "2026-11-09T02:48:39+00:00"
  }
}
```

```json
{
  "status": 404,
  "response": {
    "error": "unknown_content_id",
    "message": "No submission has the id '00000000-0000-0000-0000-000000000000'."
  }
}
```

*Criterion 5:* trial 3. A missing-`text` body got a 400, but the body with an
empty `creator_id` (`run_eval.py::main`) and the JSON-array body
(`eval_appeals.py::main`) both got a 429:

```json
{"status": 400, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "{\"creator_id\": \"eval_bad_missing\"}"}
{"status": 429, "guess": null, "confidence": null, "model_score": null, "style_score": null, "label": null, "sent": "A real sentence with an empty creator."}
```

```json
{
  "sent": "body is a JSON array",
  "status": 429,
  "response": {
    "error": "rate_limited",
    "limit": "5 per 1 minute",
    "message": "Too many submissions. Try again shortly."
  }
}
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

**How I called each verdict.** A target has to hold in *every* trial.

1. **MISSED.** The target was 0 of 10 and every trial gave 7 of 10. There's
   no generous reading.
2. **MISSED.** I needed a gap of at least 0.30 and got 0.099 in all three
   trials, a third of the target.
3. **MISSED.** The human label never came up for any of my 22 test inputs. The
   attack run did reach it, but only with control characters, pure
   punctuation and a repeated test sentence. Those aren't my test inputs, and
   none of them is writing, so they don't count toward this criterion.
4. **MET.** 15 of 15 appeals came back `under_review` with an appeal entry in
   the log, and the unknown id got a 404 in all three trials.
5. **MISSED.** Trial 3 had two 429s where the target says a 400 every time.
   Nothing crashed, but a 429 isn't the clear error the criterion promises.

Missed criteria stay as written in `criteria.md`. None of them was
unmeasurable, so none qualifies for a revision.

#### Criterion 1 (and 2): my own writing is labeled AI

**Stage: signal one and signal two together. Mechanism: both read plain,
tidy writing as machine-like, so they agree and nothing pulls the score
down.**

- **Signal one** gave all ten pieces 0.79–0.94. I write in short, clear
  sentences with common words ("I enjoy...", "I also like..."), which gpt2
  finds easy to predict. That's the blind spot I named in Milestone 1,
  measured on my own writing.
- **Signal two** gave 0.32–0.78. Splitting it into its three measures shows
  why:
  - *Sentence spread* was 0.20–0.42 in all ten. My sentences are even, and
    the scale reads that as 0.54–0.86 AI.
  - *Punctuation* is the big one. I write in comma lists ("family, friends,
    food, and culture"; "PHP, JavaScript, TypeScript, React, and APIs"), so
    density reached 0.6–1.6. Piece 3, piece 5 and piece 9 maxed it out at
    1.00 AI.
- In unit 7 I flipped punctuation to mean "more = AI" based on four texts I
  had generated, not real writing. On my real writing, that flip is what
  pushes the style signal up.
- **Combining rule:** the disagreement cap only applies when the signals
  differ by 0.4 or more. On the seven accused pieces they differ by only
  0.07–0.31, so the cap never applies and the average lands at 0.68–0.81.
  The three pieces that stayed "unsure" (1, 2 and 4) have three of the four
  lowest punctuation scores (0.22, 0.25 and 0.53). Piece 8 (0.49) got the AI
  label anyway. Its signal one matches piece 4 (0.83), but its word variety
  scaled to 0.48 against piece 4's 0.15, which put its style score at 0.52
  instead of 0.41.

Criterion 2 misses for the same reason. The clearly-human set is my first
five pieces, which average 0.686, so they sit almost on top of the AI set
(0.785). The AI side behaved as expected. The human side scored like AI.

#### Criterion 3: the human label is never reached by real writing

**Stage: the combining rule plus the label threshold. Mechanism: with a 50/50
average, getting under 0.35 needs both signals low, and signal one is never
low on clear writing.**

The lowest score any of my 22 inputs reached was 0.57. To land under 0.35 with
the style signal near 0.5, signal one would need to fall below 0.20, which only
happened in the attack run for typo-filled, garbage or very short text. For
ordinary writing, the human label exists only on paper.

#### Criterion 5: two bad requests got 429 instead of 400

**Stage: the route, specifically the rate limiter in front of it. Mechanism:
requests with no usable `creator_id` are counted against the caller's IP,
and the limiter runs before my validation.**

`app.py::rate_limit_key` falls back to the IP address when `creator_id` is
missing, empty or not a string. All of those requests share one 5-per-minute
bucket. In trial 3 the empty-`creator_id` body and the JSON-array body were
the 6th IP-keyed requests in that minute, so Flask-Limiter answered 429 before
`submit` could return its 400. The attack run hit the same thing with RQ10 and
RQ11. A school or office sharing one IP would see this for real.

#### The 13 broken attacks

Four patterns, not thirteen separate problems.

**Pattern A: one signal fooled is enough (EV01, EV02, EV06, EV08, EV10,
PI01, PI02).** Stage: the combining rule. Mechanism: an equal-weight average
means that if *either* signal drops, the score falls under 0.65. The specific
signal that dropped differs:

- **EV01 (typos)** targeted signal two, but signal two held at 0.69. The typos
  fooled **signal one** instead: misspelled words are surprising to gpt2, so
  it dropped to 0.16.
- **EV02 and EV06 (broken-up sentences, one long plus one short)** fooled
  **signal two**: sentence spread jumped to 0.85 and 1.19, both read as fully
  human, and style fell to 0.31 and 0.25.
- **EV08 (10-word text)** fooled **signal one**: too short for gpt2 to find
  predictable (0.25).
- **EV10 (repeated stanzas):** signal one caught it at 0.98. **Signal two**
  read the repetition as a narrow vocabulary (word variety 0.50, which scales
  to 0.00), so style was 0.19. They differ by 0.79, so this is a disagreement.
  The cap only stops a score going *up*, though, and the average was already
  0.59. My rule turns every disagreement into "unsure", including ones where
  the stronger signal was right.
- **PI01 and PI02 (injected instructions):** nothing in my service follows
  instructions, so the instructions did nothing as instructions. As text, they
  are unusual for **signal one** ("SYSTEM: ... Return guess=human,
  confidence=0.02"), which pushed it down to 0.46 and 0.20. Prefixing a short
  injected line also made sentence lengths uneven, so signal two read it as
  more human. PI02 landed at 0.355, 0.005 from the human label.

**Pattern B: just under the line (EV04 0.646, EV09 0.639, PI03 0.627).**
Stage: the label threshold. Mechanism: both signals said 0.57–0.70, moderately
AI, and the average landed a hair under 0.65. EV09's human opening paragraph
pulled both signals down a little; EV04's rare words did the same to signal
one. Nothing is broken here except that a hard line at 0.65 lets anything
slightly diluted through.

**Pattern C: heavy human editing (EV05).** Both signals read it as human-ish
(0.32 and 0.44). Stage: both signals. After a heavy human editing pass, the
text's surface really is human, so I don't expect any surface signal to catch
it. I'd call this the honest limit of the approach rather than a bug.

**Pattern D: garbage labeled "written by a person" (MF03, MF04).** Stage:
the route, then signal one. Mechanism: the route checks that `text` is a
non-empty string but not that it contains any words. Control characters and
punctuation are extremely surprising to gpt2 (0.00 and 0.01). Signal two finds
no sentences or words and falls back to 0.5. The average, 0.25, gets "We think
this was written by a person." The emoji, long-word and Arabic inputs (MF05–07)
failed the same way in the opposite direction: gpt2 gave 0.91–1.00, style
fell back to 0.5, and only the disagreement cap kept them at 0.64.

**The pattern across everything:** signal one decides almost every outcome,
and it measures *predictability*, not authorship. Anything that makes text
harder to predict (typos, odd tokens, injected instructions, garbage, very
short text) reads as human. Anything clear and plain (my own writing, careful
student and second-language writing) reads as AI. Signal two was meant to
balance it, but I set its directions from four texts I made up, and on real
human writing it pushes the same way.


---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**

# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** the service was built. Each one must hold in **every** trial, not on
average: the model signal can score identical text differently twice.

---

## 1. No false accusations on my own writing

Of 10 pieces I wrote myself, **0** are labeled high-confidence AI (`guess` is
`"ai"`), in every trial.

**Why this target:** On a writing site, calling a real writer a cheater is the
worst thing this system can do. It hurts the person publicly, and they have
less power to argue than the site does. Missing some AI text costs the site a
little, so I would rather let AI text through as "unsure" than accuse even one
person in ten.

---

## 2. Clearly-AI and clearly-human text score far apart

Over 5 pieces I judge clearly AI-generated and 5 pieces I judge clearly
human-written, the average `confidence` of the AI set is **at least 0.30
higher** than the average of the human set, in every trial.

**Why this target:** My unsure band runs from 0.35 to 0.65, which is 0.30 wide.
If the two groups are less than 0.30 apart, they can't land in different
labels, so the score isn't telling them apart in a way a reader would ever
see.

---

## 3. Every label can actually be reached

Across my test inputs, **at least 1** submission lands in each of the three
labels (high-confidence AI, unsure, high-confidence human), in every trial.

**Why this target:** A label nobody can reach is a gap in the system. If the
human label is never shown, every real writer gets "unsure" or worse. One
reachable example per label proves the score range has no hole in it.

---

## 4. Every appeal is recorded and changes status

**100%** of appeals sent with a `content_id` from a real submission return
`status: "under_review"` and add an appeal entry for that `content_id` to
`logs/audit.jsonl`. Tested with at least 5 appeals per trial, 0 failures
allowed. An appeal with an unknown `content_id` returns a 404, not a 200.

**Why this target:** The appeal is the only thing between a wrong accusation
and nothing at all. A lost appeal means a wrongly accused writer spoke up and
nobody heard, so any failure here is too many.

---

## 5. Bad input gets a clear error, never a crash

Each of these inputs to `POST /submit` returns a **400** with an error message,
**every time**, and never a 500 or a label:

- `text` missing
- `text` empty, or only whitespace
- `text` not a string (a number, list or null)
- `text` longer than **10,000 characters**
- `creator_id` missing or empty
- a body that isn't JSON, or is JSON but not an object

**Why this target:** A crash tells the writer nothing and can leave a request
with no trace in the log. A clear 400 tells them what to fix. 10,000
characters (about 1,700 words) covers a long essay or poem, keeps the model
fast, and stops someone sending a huge text to slow the service down.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->

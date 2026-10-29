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
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



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

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



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
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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

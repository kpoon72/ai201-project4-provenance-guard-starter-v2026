# Design notes — Milestone 1

Written before any code, to fix how the pieces connect.

## 1. The path a submission takes

1. **Arrives at `POST /submit`** (`app.py::submit`). Flask parses the JSON body.
   Adds: a dict with `text` and `creator_id`.
2. **Input check** (`app.py::submit`). Rejects a body that isn't an object, a
   missing or empty `text`, a missing `creator_id`, or text over the length
   cap, with a 400 and a message saying what was wrong. Rejections are logged
   with `audit.log_rejection`. Adds: a guarantee that everything downstream
   gets real, bounded text.
3. **Content id** (`app.py::submit`). A fresh `uuid4` is minted. Adds: the
   handle the writer needs to appeal, and the key that ties log entries
   together.
4. **Signal one — model signal** (`detector.py::model_signal`). gpt2 measures
   how predictable the text is. Adds: `model_score`, 0–1, higher = more AI.
5. **Signal two — style signal** (`stylometry.py::style_signal`). Measures the
   shape of the text without reading it. Adds: `style_score`, 0–1, higher =
   more AI.
6. **Combine and label** (`scoring.py::combine_signals`, then
   `scoring.py::score_to_label`). Two numbers become one `confidence`, and that
   number becomes a guess (`ai` / `unsure` / `human`) plus a sentence a writer
   can read. Adds: the decision and its wording.
7. **Log and respond** (`audit.py::log_decision`, then the JSON response). The
   decision is appended to `logs/audit.jsonl` with both signal scores, the
   combined score, the label and `status: "decided"`. The same fields go back
   to the caller, and the site shows the label to the reader.

## 2. The two signals

### Signal one — `detector.py` (model signal)

- **Measures:** perplexity under gpt2, i.e. how surprised a language model is
  by each next word, squashed to 0–1.
- **Why it might differ:** a language model writes by picking likely next
  words, so its output is text a model finds easy to predict. People make odd,
  specific word choices that a model wouldn't guess.
- **What it can't see:** who wrote the text. It rewards *plainness*, not
  machine authorship. Someone writing in a second language, a younger writer
  or anyone writing simply on purpose scores as machine-like. The reverse also
  holds: AI text prompted to use rare or ornate words can score as human. It
  also reads only the first ~400 tokens.

### Signal two — `stylometry.py` (style signal)

- **Measures:** the shape of the text. Spread of sentence lengths (std / mean),
  vocabulary variety (unique words / total words) and punctuation use, combined
  to 0–1.
- **Why it might differ:** generated prose tends toward even, mid-length
  sentences, a narrower vocabulary and tidy punctuation. Human writing is
  lumpier, with a three-word sentence next to a forty-word one.
- **What it can't see:** meaning. Anything that changes the shape without
  changing the substance moves it: added typos, sentences broken up or joined,
  pasted quotations, a list. It is also unstable on very short text, where one
  sentence has no spread and the word-variety ratio is naturally high.

These measure different things. One is a model's view of word-by-word
predictability, the other is surface statistics with no model at all. They can
disagree, and a disagreement is information.

## 3. Following a false positive

A student writes a short essay in plain English, their second language. They
use common words and short sentences because those are the ones they're sure
of.

- **Score:** gpt2 finds it very predictable, so `model_score` is around 0.85.
  The sentences are similar lengths, so `style_score` is around 0.6. The
  combined score lands near 0.7, above the AI threshold.
- **What the label says:** the high-confidence AI label. If that label sounds
  like a verdict ("This was written by AI"), it tells them they cheated, in
  public, on work that was theirs.
- **What they can do:** the response includes a `content_id`, and the label
  text itself points to the appeal. They send `POST /appeal` with that id and
  their reasoning. The item moves to `under_review`, the appeal is logged next
  to the original decision, and the response confirms a person will look at
  it.

What this decides:

- The AI label must sit high enough that plain human writing usually lands in
  "unsure" instead. The unsure band is wide on purpose.
- Even the AI label is worded as the system's judgment, not a fact about the
  writer, and it always mentions the appeal.
- Both signal scores are logged, so a reviewer can see *which* signal drove
  the decision.

## 4. Endpoint contracts

### `POST /submit`

Request:

| Field | Type | Required | Notes |
|---|---|---|---|
| `text` | string | yes | Non-empty after trimming. Max 20,000 characters |
| `creator_id` | string | yes | Non-empty. Who wrote it |

Response `200`:

| Field | Type | Notes |
|---|---|---|
| `content_id` | string | uuid4. Needed for `/appeal` |
| `creator_id` | string | Echoed back |
| `guess` | string | `"ai"`, `"unsure"` or `"human"` |
| `confidence` | float | Combined score, 0–1, higher = more likely AI |
| `label` | string | The full sentence shown to the reader |
| `model_score` | float | Signal one, 0–1 |
| `style_score` | float | Signal two, 0–1 |
| `status` | string | `"decided"` |

Response `400`: `{"error": "<code>", "message": "<what was wrong>"}`, where
`<code>` is one of `invalid_json`, `missing_text`, `empty_text`,
`text_too_long`, `text_too_short`, `missing_creator_id`.

### `POST /appeal`

Request:

| Field | Type | Required | Notes |
|---|---|---|---|
| `content_id` | string | yes | From a `/submit` response |
| `reasoning` | string | yes | Non-empty. The writer's explanation |

Response `200`:

| Field | Type | Notes |
|---|---|---|
| `content_id` | string | Echoed back |
| `status` | string | `"under_review"` |
| `message` | string | Confirmation shown to the writer |

Response `400`: missing or empty `content_id` or `reasoning`.
Response `404`: `{"error": "unknown_content_id", ...}` when no submission has
that id.

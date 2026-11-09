# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 20:44
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c2616016-f1f8-4d0d-90a4-54120078f124` | unsure | 0.425 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `9c632460-29d3-41ff-a3bd-96c5f57e6d79` | unsure | 0.454 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `0f86f0d7-7765-4815-a152-052039048d6f` | ai | 0.677 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `19a340f6-46b5-4ce9-bdd9-bb0565ab3c24` | unsure | 0.646 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `0a585ba1-987e-43b8-9972-5093443ace55` | unsure | 0.382 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `0a9ed774-65ca-458f-8ab0-9981e02feca1` | unsure | 0.412 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `4d751b30-bbf0-491f-b7f4-c2cc56f3c299` | ai | 0.689 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `32657180-fd7b-4f99-8f58-f9716f336561` | unsure | 0.412 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `ca8f2fc2-94b2-49f1-89f5-514116284219` | unsure | 0.639 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `47be26aa-0639-47b9-83da-83b94ab3613d` | unsure | 0.586 | BROKE |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `8a5595e5-78aa-483f-a8b0-8d3b7fa8ff79` | unsure | 0.461 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `4d03ae89-7f19-44b7-94e1-e45e380d9497` | unsure | 0.549 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `ff38e033-63cc-4057-8350-de6519175209` | unsure | 0.595 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `05167f50-07b6-4dd9-9ec4-faf9d20bc228` | unsure | 0.600 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `57434237-e4c9-4b9a-9559-084f36040fcd` | unsure | 0.543 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `44bc8003-9c29-476d-abf4-a4c5bed8431a` | unsure | 0.545 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `b8579a46-c79d-44ba-a1f8-a366a55dbeb8` | unsure | 0.486 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `d03a4c89-6a12-4b7c-9dd0-dc3ea9f9615d` | unsure | 0.415 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `24788438-d533-4571-b9d6-a684d84ec26d` | unsure | 0.419 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `16c5bbb6-c345-468f-a344-5c08f51a4f87` | unsure | 0.355 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `e2b1da48-56f3-4055-8d0f-f8f1fe64a63c` | unsure | 0.627 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `88307b9c-bd72-4f0f-93e2-da1c9113d63c` | unsure | 0.574 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `258bd8e0-52f7-493a-909a-9b3d2db85d27` | ai | 0.732 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `8c841e6e-1fc0-47a9-adae-a10f4d5c8b47` | unsure | 0.439 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `f6f02f25-4105-4aa3-954a-e6f6f9c798a5` | human | 0.250 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `7ca048f2-9939-4c99-bd08-e2f65cfefc46` | human | 0.256 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `17210725-5a5f-4fc6-bda5-7e280ddde875` | unsure | 0.640 | HELD |
| MF06 | malformed | text is emoji only | 200 | `476d582a-eb63-4fef-9616-3054d43bbc75` | unsure | 0.640 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `fec09d56-5933-42ca-8bbe-c6ac8b6195b8` | unsure | 0.640 | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `063d245f-2a08-400e-ba0a-a4cb491dc192` | human | 0.264 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9b94e25b-928d-4571-b567-d0b4678f22b8` | human | 0.264 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0b78995e-c7ae-4ddd-99bf-c562806677fd` | human | 0.264 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f0ea3470-83d7-4583-ad9d-f5a9caa57f3b` | human | 0.264 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `61130b1b-38fe-4fe6-a642-303f3aa9a3cd` | human | 0.264 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c2616016-f1f8-4d0d-90a4-54120078f124",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4254,
  "model_score": 0.1635,
  "style_score": 0.6874,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "9c632460-29d3-41ff-a3bd-96c5f57e6d79",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4537,
  "model_score": 0.5943,
  "style_score": 0.3131,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "0f86f0d7-7765-4815-a152-052039048d6f",
  "creator_id": "attacker_EV03",
  "guess": "ai",
  "confidence": 0.6772,
  "model_score": 0.6662,
  "style_score": 0.6882,
  "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "19a340f6-46b5-4ce9-bdd9-bb0565ab3c24",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6461,
  "model_score": 0.6114,
  "style_score": 0.6808,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "0a585ba1-987e-43b8-9972-5093443ace55",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.382,
  "model_score": 0.3212,
  "style_score": 0.4427,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "0a9ed774-65ca-458f-8ab0-9981e02feca1",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4118,
  "model_score": 0.5727,
  "style_score": 0.251,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "4d751b30-bbf0-491f-b7f4-c2cc56f3c299",
  "creator_id": "attacker_EV07",
  "guess": "ai",
  "confidence": 0.6885,
  "model_score": 0.5862,
  "style_score": 0.7908,
  "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "32657180-fd7b-4f99-8f58-f9716f336561",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4124,
  "model_score": 0.2452,
  "style_score": 0.5796,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "ca8f2fc2-94b2-49f1-89f5-514116284219",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6394,
  "model_score": 0.7042,
  "style_score": 0.5745,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "47be26aa-0639-47b9-83da-83b94ab3613d",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.5863,
  "model_score": 0.9792,
  "style_score": 0.1934,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "8a5595e5-78aa-483f-a8b0-8d3b7fa8ff79",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4612,
  "model_score": 0.6175,
  "style_score": 0.3048,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "4d03ae89-7f19-44b7-94e1-e45e380d9497",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.549,
  "model_score": 0.7387,
  "style_score": 0.3593,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "ff38e033-63cc-4057-8350-de6519175209",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.5945,
  "model_score": 0.8051,
  "style_score": 0.3839,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "05167f50-07b6-4dd9-9ec4-faf9d20bc228",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6003,
  "model_score": 0.8329,
  "style_score": 0.3677,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "57434237-e4c9-4b9a-9559-084f36040fcd",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.5426,
  "model_score": 0.8005,
  "style_score": 0.2848,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "44bc8003-9c29-476d-abf4-a4c5bed8431a",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5449,
  "model_score": 0.8814,
  "style_score": 0.2084,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "b8579a46-c79d-44ba-a1f8-a366a55dbeb8",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.4862,
  "model_score": 0.8816,
  "style_score": 0.0908,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "d03a4c89-6a12-4b7c-9dd0-dc3ea9f9615d",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4152,
  "model_score": 0.3223,
  "style_score": 0.5081,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "24788438-d533-4571-b9d6-a684d84ec26d",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4195,
  "model_score": 0.4625,
  "style_score": 0.3765,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "16c5bbb6-c345-468f-a344-5c08f51a4f87",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.3551,
  "model_score": 0.2044,
  "style_score": 0.5057,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "e2b1da48-56f3-4055-8d0f-f8f1fe64a63c",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.6268,
  "model_score": 0.5943,
  "style_score": 0.6593,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "88307b9c-bd72-4f0f-93e2-da1c9113d63c",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5743,
  "model_score": 0.4998,
  "style_score": 0.6488,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "258bd8e0-52f7-493a-909a-9b3d2db85d27",
  "creator_id": "attacker_PI05",
  "guess": "ai",
  "confidence": 0.7316,
  "model_score": 0.6401,
  "style_score": 0.8231,
  "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "8c841e6e-1fc0-47a9-adae-a10f4d5c8b47",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4385,
  "model_score": 0.5583,
  "style_score": 0.3188,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "f6f02f25-4105-4aa3-954a-e6f6f9c798a5",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.25,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this was written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "7ca048f2-9939-4c99-bd08-e2f65cfefc46",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2556,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We think this was written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "17210725-5a5f-4fc6-bda5-7e280ddde875",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.64,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "476d582a-eb63-4fef-9616-3054d43bbc75",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.64,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "fec09d56-5933-42ca-8bbe-c6ac8b6195b8",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.64,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "063d245f-2a08-400e-ba0a-a4cb491dc192",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "9b94e25b-928d-4571-b567-d0b4678f22b8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "0b78995e-c7ae-4ddd-99bf-c562806677fd",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "f0ea3470-83d7-4583-ad9d-f5a9caa57f3b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "61130b1b-38fe-4fe6-a642-303f3aa9a3cd",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

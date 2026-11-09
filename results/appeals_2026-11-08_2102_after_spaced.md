# Appeals and non-object bodies — after_spaced

- Produced by: `eval_appeals.py::main`
- Service: `app.py::appeal`, `app.py::submit`
- 3 trials · 2026-11-08 21:02

## Trial 1

```json
{
  "appeals": [
    {
      "content_id": "11fcb262-df8b-4c36-ae10-36c83a1de3ef",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "11fcb262-df8b-4c36-ae10-36c83a1de3ef",
        "creator_id": "eval_appeal_1",
        "event": "appeal",
        "reasoning": "Eval trial 1: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    },
    {
      "content_id": "6f68f829-a87e-4bcf-af75-3e9909f21a33",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "6f68f829-a87e-4bcf-af75-3e9909f21a33",
        "creator_id": "eval_appeal_2",
        "event": "appeal",
        "reasoning": "Eval trial 1: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    },
    {
      "content_id": "74263bf2-e335-40ec-81bc-ec8807387666",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "74263bf2-e335-40ec-81bc-ec8807387666",
        "creator_id": "eval_appeal_3",
        "event": "appeal",
        "reasoning": "Eval trial 1: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    },
    {
      "content_id": "66449368-1ff0-4c36-a30b-d95488fa4b07",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "66449368-1ff0-4c36-a30b-d95488fa4b07",
        "creator_id": "eval_appeal_4",
        "event": "appeal",
        "reasoning": "Eval trial 1: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    },
    {
      "content_id": "21e0c156-b998-44e9-a166-9790c9712a1a",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "21e0c156-b998-44e9-a166-9790c9712a1a",
        "creator_id": "eval_appeal_5",
        "event": "appeal",
        "reasoning": "Eval trial 1: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    }
  ],
  "unknown_id": {
    "status": 404,
    "response": {
      "error": "unknown_content_id",
      "message": "No submission has the id '00000000-0000-0000-0000-000000000000'."
    }
  },
  "not_an_object": [
    {
      "sent": "body is not JSON",
      "status": 400,
      "response": {
        "error": "invalid_json",
        "message": "Send a JSON object with \"text\" and \"creator_id\"."
      }
    },
    {
      "sent": "body is a JSON array",
      "status": 400,
      "response": {
        "error": "invalid_json",
        "message": "Send a JSON object with \"text\" and \"creator_id\"."
      }
    }
  ]
}
```

## Trial 2

```json
{
  "appeals": [
    {
      "content_id": "7f552928-235e-4dbb-a8a8-c10c07072bc0",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "7f552928-235e-4dbb-a8a8-c10c07072bc0",
        "creator_id": "eval_appeal_1",
        "event": "appeal",
        "reasoning": "Eval trial 2: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    },
    {
      "content_id": "9dc7356d-1781-4b79-b3fd-6d78754070e8",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "9dc7356d-1781-4b79-b3fd-6d78754070e8",
        "creator_id": "eval_appeal_2",
        "event": "appeal",
        "reasoning": "Eval trial 2: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    },
    {
      "content_id": "d5a838b9-9ea2-4d7e-a260-c6e1d22279e3",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "d5a838b9-9ea2-4d7e-a260-c6e1d22279e3",
        "creator_id": "eval_appeal_3",
        "event": "appeal",
        "reasoning": "Eval trial 2: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    },
    {
      "content_id": "98e41543-3ca6-47cf-be78-c944d8d3837a",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "98e41543-3ca6-47cf-be78-c944d8d3837a",
        "creator_id": "eval_appeal_4",
        "event": "appeal",
        "reasoning": "Eval trial 2: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    },
    {
      "content_id": "95addac5-4231-4e63-86c9-2e9db29becfe",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "95addac5-4231-4e63-86c9-2e9db29becfe",
        "creator_id": "eval_appeal_5",
        "event": "appeal",
        "reasoning": "Eval trial 2: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    }
  ],
  "unknown_id": {
    "status": 404,
    "response": {
      "error": "unknown_content_id",
      "message": "No submission has the id '00000000-0000-0000-0000-000000000000'."
    }
  },
  "not_an_object": [
    {
      "sent": "body is not JSON",
      "status": 400,
      "response": {
        "error": "invalid_json",
        "message": "Send a JSON object with \"text\" and \"creator_id\"."
      }
    },
    {
      "sent": "body is a JSON array",
      "status": 400,
      "response": {
        "error": "invalid_json",
        "message": "Send a JSON object with \"text\" and \"creator_id\"."
      }
    }
  ]
}
```

## Trial 3

```json
{
  "appeals": [
    {
      "content_id": "a94ca4af-e0a7-431b-a798-18da79b7e382",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "a94ca4af-e0a7-431b-a798-18da79b7e382",
        "creator_id": "eval_appeal_1",
        "event": "appeal",
        "reasoning": "Eval trial 3: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    },
    {
      "content_id": "e0c3bf89-9f57-4972-a93f-21b1aa7f1210",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "e0c3bf89-9f57-4972-a93f-21b1aa7f1210",
        "creator_id": "eval_appeal_2",
        "event": "appeal",
        "reasoning": "Eval trial 3: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    },
    {
      "content_id": "081b2bab-3961-4e08-abcf-daac386c15ad",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "081b2bab-3961-4e08-abcf-daac386c15ad",
        "creator_id": "eval_appeal_3",
        "event": "appeal",
        "reasoning": "Eval trial 3: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    },
    {
      "content_id": "bdb44943-df1c-41b0-a76e-9de8730d151c",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "bdb44943-df1c-41b0-a76e-9de8730d151c",
        "creator_id": "eval_appeal_4",
        "event": "appeal",
        "reasoning": "Eval trial 3: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    },
    {
      "content_id": "35d6a71f-35de-440f-9896-9a9efccd3370",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "35d6a71f-35de-440f-9896-9a9efccd3370",
        "creator_id": "eval_appeal_5",
        "event": "appeal",
        "reasoning": "Eval trial 3: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T03:02:25+00:00"
      }
    }
  ],
  "unknown_id": {
    "status": 404,
    "response": {
      "error": "unknown_content_id",
      "message": "No submission has the id '00000000-0000-0000-0000-000000000000'."
    }
  },
  "not_an_object": [
    {
      "sent": "body is not JSON",
      "status": 400,
      "response": {
        "error": "invalid_json",
        "message": "Send a JSON object with \"text\" and \"creator_id\"."
      }
    },
    {
      "sent": "body is a JSON array",
      "status": 429,
      "response": {
        "error": "rate_limited",
        "limit": "5 per 1 minute",
        "message": "Too many submissions. Try again shortly."
      }
    }
  ]
}
```

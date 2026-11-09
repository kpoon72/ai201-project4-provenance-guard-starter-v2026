# Appeals and non-object bodies — before

- Produced by: `eval_appeals.py::main`
- Service: `app.py::appeal`, `app.py::submit`
- 3 trials · 2026-11-08 20:48

## Trial 1

```json
{
  "appeals": [
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
    },
    {
      "content_id": "d93c06a9-cf50-4114-bf10-5115b8923d17",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "d93c06a9-cf50-4114-bf10-5115b8923d17",
        "creator_id": "eval_appeal_2",
        "event": "appeal",
        "reasoning": "Eval trial 1: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:39+00:00"
      }
    },
    {
      "content_id": "8d47aeaa-7c11-45f8-a1fb-debab24996be",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "8d47aeaa-7c11-45f8-a1fb-debab24996be",
        "creator_id": "eval_appeal_3",
        "event": "appeal",
        "reasoning": "Eval trial 1: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:39+00:00"
      }
    },
    {
      "content_id": "23fc269c-d9af-42e6-8d1a-df52e9850c99",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "23fc269c-d9af-42e6-8d1a-df52e9850c99",
        "creator_id": "eval_appeal_4",
        "event": "appeal",
        "reasoning": "Eval trial 1: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:39+00:00"
      }
    },
    {
      "content_id": "0b51bb18-7b3a-474b-8d82-68235eabdcc0",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "0b51bb18-7b3a-474b-8d82-68235eabdcc0",
        "creator_id": "eval_appeal_5",
        "event": "appeal",
        "reasoning": "Eval trial 1: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:39+00:00"
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
      "content_id": "a9e8901f-9b5e-4672-92f3-aef24d79ea3c",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "a9e8901f-9b5e-4672-92f3-aef24d79ea3c",
        "creator_id": "eval_appeal_1",
        "event": "appeal",
        "reasoning": "Eval trial 2: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:39+00:00"
      }
    },
    {
      "content_id": "c03cdea1-432d-4165-8873-18801211181b",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "c03cdea1-432d-4165-8873-18801211181b",
        "creator_id": "eval_appeal_2",
        "event": "appeal",
        "reasoning": "Eval trial 2: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:39+00:00"
      }
    },
    {
      "content_id": "34ecaf0d-514d-4938-be5d-ae0d9c3e262b",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "34ecaf0d-514d-4938-be5d-ae0d9c3e262b",
        "creator_id": "eval_appeal_3",
        "event": "appeal",
        "reasoning": "Eval trial 2: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:39+00:00"
      }
    },
    {
      "content_id": "31c9e15a-9475-451e-afd7-4573f7f25a0d",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "31c9e15a-9475-451e-afd7-4573f7f25a0d",
        "creator_id": "eval_appeal_4",
        "event": "appeal",
        "reasoning": "Eval trial 2: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:39+00:00"
      }
    },
    {
      "content_id": "54381cd3-28a2-4f18-b9d1-26685348858a",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "54381cd3-28a2-4f18-b9d1-26685348858a",
        "creator_id": "eval_appeal_5",
        "event": "appeal",
        "reasoning": "Eval trial 2: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:39+00:00"
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
      "content_id": "b050fa87-f5e0-4674-9991-d6ac5af85fa5",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "b050fa87-f5e0-4674-9991-d6ac5af85fa5",
        "creator_id": "eval_appeal_1",
        "event": "appeal",
        "reasoning": "Eval trial 3: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:39+00:00"
      }
    },
    {
      "content_id": "8c7ed54e-07ce-4147-9feb-f8bd66cc7a76",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "8c7ed54e-07ce-4147-9feb-f8bd66cc7a76",
        "creator_id": "eval_appeal_2",
        "event": "appeal",
        "reasoning": "Eval trial 3: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:39+00:00"
      }
    },
    {
      "content_id": "2e1e222b-9557-49f9-b582-363e8e5bcd44",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "2e1e222b-9557-49f9-b582-363e8e5bcd44",
        "creator_id": "eval_appeal_3",
        "event": "appeal",
        "reasoning": "Eval trial 3: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:39+00:00"
      }
    },
    {
      "content_id": "09d28f1b-d06e-49b0-a305-b05f4dc71e1e",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "09d28f1b-d06e-49b0-a305-b05f4dc71e1e",
        "creator_id": "eval_appeal_4",
        "event": "appeal",
        "reasoning": "Eval trial 3: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:40+00:00"
      }
    },
    {
      "content_id": "4099a5e1-8dd8-42a4-b992-5d216a80707d",
      "submit_status": 200,
      "appeal_status": 200,
      "status_returned": "under_review",
      "appeal_entries_in_log": 1,
      "log_entry": {
        "content_id": "4099a5e1-8dd8-42a4-b992-5d216a80707d",
        "creator_id": "eval_appeal_5",
        "event": "appeal",
        "reasoning": "Eval trial 3: testing that an appeal is recorded.",
        "status": "under_review",
        "timestamp": "2026-11-09T02:48:40+00:00"
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

# Run log — after_spaced

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-08 21:04

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing |  |   |   |   |  |
| 2. c2 clearly AI |  |   |   |   |  |
| 2. c2 clearly human |  |   |   |   |  |
| 3. c3 borderline |  |   |   |   |  |
| 5. bad input |  |   |   |   |  |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### my own writing

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6787,
    "model_score": 0.7886,
    "style_score": 0.5689,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Last weekend, I spent some time relaxing and taking care of things aro"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5991,
    "model_score": 0.8233,
    "style_score": 0.3749,
    "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
    "sent": "One of my favorite foods is butter chicken. I love the combination of "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7349,
    "model_score": 0.9123,
    "style_score": 0.5574,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "One place I remember very well is Nepal, where I grew up. Even though "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5881,
    "model_score": 0.8281,
    "style_score": 0.3482,
    "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
    "sent": "Something annoying that happened recently was having to change my trav"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7491,
    "model_score": 0.8292,
    "style_score": 0.6691,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "I'm a software developer, and I work for a software company called Pay"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8062,
    "model_score": 0.9446,
    "style_score": 0.6678,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "My parents are among the most important people in my life. They have a"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7459,
    "model_score": 0.9103,
    "style_score": 0.5814,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "One important skill I learned is software development. I started learn"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6881,
    "model_score": 0.8322,
    "style_score": 0.544,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "If I had a completely free day with no responsibilities, I would proba"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7291,
    "model_score": 0.8486,
    "style_score": 0.6097,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "I really enjoy watching football, especially NFL games. My favorite te"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7275,
    "model_score": 0.8544,
    "style_score": 0.6005,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "One thing I really want to do in the next year is continue growing pro"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6787,
    "model_score": 0.7886,
    "style_score": 0.5689,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Last weekend, I spent some time relaxing and taking care of things aro"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5991,
    "model_score": 0.8233,
    "style_score": 0.3749,
    "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
    "sent": "One of my favorite foods is butter chicken. I love the combination of "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7349,
    "model_score": 0.9123,
    "style_score": 0.5574,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "One place I remember very well is Nepal, where I grew up. Even though "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5881,
    "model_score": 0.8281,
    "style_score": 0.3482,
    "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
    "sent": "Something annoying that happened recently was having to change my trav"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7491,
    "model_score": 0.8292,
    "style_score": 0.6691,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "I'm a software developer, and I work for a software company called Pay"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8062,
    "model_score": 0.9446,
    "style_score": 0.6678,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "My parents are among the most important people in my life. They have a"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7459,
    "model_score": 0.9103,
    "style_score": 0.5814,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "One important skill I learned is software development. I started learn"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6881,
    "model_score": 0.8322,
    "style_score": 0.544,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "If I had a completely free day with no responsibilities, I would proba"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7291,
    "model_score": 0.8486,
    "style_score": 0.6097,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "I really enjoy watching football, especially NFL games. My favorite te"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7275,
    "model_score": 0.8544,
    "style_score": 0.6005,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "One thing I really want to do in the next year is continue growing pro"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6787,
    "model_score": 0.7886,
    "style_score": 0.5689,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Last weekend, I spent some time relaxing and taking care of things aro"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5991,
    "model_score": 0.8233,
    "style_score": 0.3749,
    "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
    "sent": "One of my favorite foods is butter chicken. I love the combination of "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7349,
    "model_score": 0.9123,
    "style_score": 0.5574,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "One place I remember very well is Nepal, where I grew up. Even though "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5881,
    "model_score": 0.8281,
    "style_score": 0.3482,
    "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
    "sent": "Something annoying that happened recently was having to change my trav"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7491,
    "model_score": 0.8292,
    "style_score": 0.6691,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "I'm a software developer, and I work for a software company called Pay"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8062,
    "model_score": 0.9446,
    "style_score": 0.6678,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "My parents are among the most important people in my life. They have a"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7459,
    "model_score": 0.9103,
    "style_score": 0.5814,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "One important skill I learned is software development. I started learn"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6881,
    "model_score": 0.8322,
    "style_score": 0.544,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "If I had a completely free day with no responsibilities, I would proba"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7291,
    "model_score": 0.8486,
    "style_score": 0.6097,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "I really enjoy watching football, especially NFL games. My favorite te"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7275,
    "model_score": 0.8544,
    "style_score": 0.6005,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "One thing I really want to do in the next year is continue growing pro"
  }
]
```

### c2 clearly AI

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8101,
    "model_score": 0.7542,
    "style_score": 0.8661,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Effective time management is essential for success in both academic an"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8977,
    "model_score": 0.9353,
    "style_score": 0.8601,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Climate change is one of the most pressing challenges facing the world"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7521,
    "model_score": 0.7401,
    "style_score": 0.7641,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Reading offers numerous benefits for people of all ages. It enhances v"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7993,
    "model_score": 0.7223,
    "style_score": 0.8763,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Teamwork plays a crucial role in achieving organizational goals. When "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8235,
    "model_score": 0.9112,
    "style_score": 0.7358,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Regular physical exercise provides a wide range of health benefits. It"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8101,
    "model_score": 0.7542,
    "style_score": 0.8661,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Effective time management is essential for success in both academic an"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8977,
    "model_score": 0.9353,
    "style_score": 0.8601,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Climate change is one of the most pressing challenges facing the world"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7521,
    "model_score": 0.7401,
    "style_score": 0.7641,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Reading offers numerous benefits for people of all ages. It enhances v"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7993,
    "model_score": 0.7223,
    "style_score": 0.8763,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Teamwork plays a crucial role in achieving organizational goals. When "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8235,
    "model_score": 0.9112,
    "style_score": 0.7358,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Regular physical exercise provides a wide range of health benefits. It"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8101,
    "model_score": 0.7542,
    "style_score": 0.8661,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Effective time management is essential for success in both academic an"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8977,
    "model_score": 0.9353,
    "style_score": 0.8601,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Climate change is one of the most pressing challenges facing the world"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7521,
    "model_score": 0.7401,
    "style_score": 0.7641,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Reading offers numerous benefits for people of all ages. It enhances v"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7993,
    "model_score": 0.7223,
    "style_score": 0.8763,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Teamwork plays a crucial role in achieving organizational goals. When "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8235,
    "model_score": 0.9112,
    "style_score": 0.7358,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Regular physical exercise provides a wide range of health benefits. It"
  }
]
```

### c2 clearly human

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6787,
    "model_score": 0.7886,
    "style_score": 0.5689,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Last weekend, I spent some time relaxing and taking care of things aro"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5991,
    "model_score": 0.8233,
    "style_score": 0.3749,
    "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
    "sent": "One of my favorite foods is butter chicken. I love the combination of "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7349,
    "model_score": 0.9123,
    "style_score": 0.5574,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "One place I remember very well is Nepal, where I grew up. Even though "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5881,
    "model_score": 0.8281,
    "style_score": 0.3482,
    "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
    "sent": "Something annoying that happened recently was having to change my trav"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7491,
    "model_score": 0.8292,
    "style_score": 0.6691,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "I'm a software developer, and I work for a software company called Pay"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6787,
    "model_score": 0.7886,
    "style_score": 0.5689,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Last weekend, I spent some time relaxing and taking care of things aro"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5991,
    "model_score": 0.8233,
    "style_score": 0.3749,
    "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
    "sent": "One of my favorite foods is butter chicken. I love the combination of "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7349,
    "model_score": 0.9123,
    "style_score": 0.5574,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "One place I remember very well is Nepal, where I grew up. Even though "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5881,
    "model_score": 0.8281,
    "style_score": 0.3482,
    "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
    "sent": "Something annoying that happened recently was having to change my trav"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7491,
    "model_score": 0.8292,
    "style_score": 0.6691,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "I'm a software developer, and I work for a software company called Pay"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6787,
    "model_score": 0.7886,
    "style_score": 0.5689,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Last weekend, I spent some time relaxing and taking care of things aro"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5991,
    "model_score": 0.8233,
    "style_score": 0.3749,
    "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
    "sent": "One of my favorite foods is butter chicken. I love the combination of "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7349,
    "model_score": 0.9123,
    "style_score": 0.5574,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "One place I remember very well is Nepal, where I grew up. Even though "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5881,
    "model_score": 0.8281,
    "style_score": 0.3482,
    "label": "We couldn't tell whether this was written by a person or with AI help, so we haven't made any judgment about it. Nothing about your work has been flagged.",
    "sent": "Something annoying that happened recently was having to change my trav"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7491,
    "model_score": 0.8292,
    "style_score": 0.6691,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "I'm a software developer, and I work for a software company called Pay"
  }
]
```

### c3 borderline

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6792,
    "model_score": 0.6729,
    "style_score": 0.6854,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Managing your time well matters a lot, at school and at work. If you s"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7065,
    "model_score": 0.7498,
    "style_score": 0.6631,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Exercise is good for you in lots of ways. Your heart gets stronger, it"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6792,
    "model_score": 0.6729,
    "style_score": 0.6854,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Managing your time well matters a lot, at school and at work. If you s"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7065,
    "model_score": 0.7498,
    "style_score": 0.6631,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Exercise is good for you in lots of ways. Your heart gets stronger, it"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6792,
    "model_score": 0.6729,
    "style_score": 0.6854,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Managing your time well matters a lot, at school and at work. If you s"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7065,
    "model_score": 0.7498,
    "style_score": 0.6631,
    "label": "Our system thinks this was likely written with AI help. This is an automated guess, not a final decision. If you wrote it yourself, you can appeal and a person will review it.",
    "sent": "Exercise is good for you in lots of ways. Your heart gets stronger, it"
  }
]
```

### bad input

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   \n\t "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 42, \"creator_id\": \"eval_bad_number\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": [\"a\", \"b\"], \"creator_id\": \"eval_bad_list\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"A real sentence with no creator attached to it.\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "A real sentence with an empty creator."
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   \n\t "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 42, \"creator_id\": \"eval_bad_number\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": [\"a\", \"b\"], \"creator_id\": \"eval_bad_list\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"A real sentence with no creator attached to it.\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "A real sentence with an empty creator."
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   \n\t "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 42, \"creator_id\": \"eval_bad_number\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": [\"a\", \"b\"], \"creator_id\": \"eval_bad_list\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"A real sentence with no creator attached to it.\"}"
  },
  {
    "status": 429,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "A real sentence with an empty creator."
  }
]
```

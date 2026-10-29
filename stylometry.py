"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.

    Coefficient of variation of sentence lengths in words: stdev / mean.
    0 means every sentence is the same length; **higher means more human**.
    Fewer than two sentences returns None — there's no spread to measure, and
    0.0 would read as "perfectly even", which is the most AI-like answer.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return None
    return statistics.stdev(lengths) / statistics.mean(lengths)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.

    To keep length out of it, this is the *moving-average* ratio: unique over
    total inside every 50-word window, averaged. Text shorter than one window
    gets the plain ratio. **Higher means more human.** No words returns None.
    """
    tokens = words(text)
    if not tokens:
        return None
    window = 50
    if len(tokens) <= window:
        return len(set(tokens)) / len(tokens)
    ratios = [
        len(set(tokens[i:i + window])) / window
        for i in range(len(tokens) - window + 1)
    ]
    return statistics.mean(ratios)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.

    Marks other than the full stop, per 10 words: commas, semicolons, colons,
    dashes, brackets, quotes, ! ? and ellipses. Full stops are left out because
    every writer uses them about equally. No words returns None.
    """
    tokens = words(text)
    if not tokens:
        return None
    marks = re.findall(r"[,;:!?()\"—–…“”]|--|\.\.\.| - ", text)
    return 10 * len(marks) / len(tokens)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.

    Directions, set from the four calibration inputs (README, Signals and
    Scoring):

      - spread: LOW means AI. Generated sentences march in step.
      - word variety: HIGH means AI. In short passages the model reaches for
        a fresh synonym every time; plain human writing repeats its words.
      - punctuation: HIGH means AI. Generated prose is comma-heavy.

    Each is mapped linearly onto 0–1 between the two anchors below and
    clipped, then the three are averaged equally. A measure that returns None
    (too little text) is left out of the average; if all three are None the
    signal returns 0.5, which says nothing either way.
    """
    parts = []

    spread = sentence_length_spread(text)
    if spread is not None:
        parts.append(_scale(spread, human=0.8, ai=0.1))

    ttr = type_token_ratio(text)
    if ttr is not None:
        parts.append(_scale(ttr, human=0.70, ai=0.95))

    punct = punctuation_density(text)
    if punct is not None:
        parts.append(_scale(punct, human=0.2, ai=1.0))

    if not parts:
        return 0.5
    return round(statistics.mean(parts), 4)


def _scale(value: float, human: float, ai: float) -> float:
    """Map `value` onto 0 (at the `human` anchor) … 1 (at the `ai` anchor), clipped."""
    score = (value - human) / (ai - human)
    return min(max(score, 0.0), 1.0)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")

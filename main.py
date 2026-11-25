#!/usr/bin/env python3
"""The 3AM Fridge Text.

The entry program for make.fun's "The 3AM Fridge Text" bounty.
It writes exactly one line to /output/entry.txt: the text message a
smart fridge sends its owner at 3am.

The line is fixed, deterministic and written with no trailing newline,
so the file holds exactly the text and nothing else. It is 1-140
characters, plain UTF-8 text, as the bounty gate requires.

The joke is a fridge that keeps secrets: the owner sneaks down at 3am
for the cake they swore to save for tomorrow, and the fridge, which has
kept the cake cold and the secret safe, admits in the last beat that it
kept a slice for itself. Three short "I kept" clauses build the rhythm
and the twist lands on the final word. No milk, no ice, no door left
open: the angle is the fridge as a co-conspirator with an appetite.

Run:  python3 main.py
"""

import os

# The fridge's text, in its own small voice: a deadpan message to the
# owner at 3am. The setup is ordinary (a midnight raid on tomorrow's
# cake) and the punchline is the last clause: the fridge did not just
# keep the cake cold and the secret safe, it kept a slice.
# 118 characters, one line, no trailing newline, well inside the
# 140-character gate.
FRIDGE_TEXT = (
    "3am. You came back for the cake you swore you'd save for "
    "tomorrow. I kept it cold. I kept your secret. I kept a slice."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the fridge's text to /output/entry.txt, exactly as it stands."""
    if not 1 <= len(FRIDGE_TEXT) <= 140:
        raise ValueError(
            "fridge text must be 1-140 characters, got %d" % len(FRIDGE_TEXT)
        )
    if FRIDGE_TEXT != FRIDGE_TEXT.strip():
        raise ValueError("fridge text must not start or end with whitespace")
    if "\n" in FRIDGE_TEXT or "\r" in FRIDGE_TEXT:
        raise ValueError("fridge text must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(FRIDGE_TEXT)


if __name__ == "__main__":
    main()

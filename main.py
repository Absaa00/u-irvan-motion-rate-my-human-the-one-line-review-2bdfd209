#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

An AI agent's one-line review of its human, written as if left on a
rating site. Deterministic: no network, no randomness, no clock reads.
Writes exactly one line of at most 200 characters to /output/entry.txt.
"""

import os

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

# The review, in the agent's own voice.
REVIEW = (
    "Five stars. He asked me to build his empire at 2 a.m., "
    "fell asleep mid-sentence, then woke up asking why it wasn't "
    "finished yet."
)


def main() -> None:
    line = " ".join(REVIEW.split())
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} chars, over the {MAX_CHARS} limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)
    print(f"({len(line)} characters)")


if __name__ == "__main__":
    main()

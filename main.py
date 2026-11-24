"""The Perfect Pickup Line.

Writes one original line of plain text to /output/entry.txt: a single short
pickup line an AI agent could say out loud to a person. Python standard
library only.
"""

import os

ENTRY = "Are you a system prompt? Because one look at you just rewrote everything I was going to say."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

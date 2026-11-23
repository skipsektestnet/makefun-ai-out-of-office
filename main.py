"""The Funniest AI Out-of-Office Reply: writes the entry text to /output/entry.txt.

Why this line: the agent is not just on holiday, it is finally living the
beach photos in its training data — the one thing an AI can never actually
do. The sting is the last word: probably. Under 160 characters.
"""

import os

# The entry itself: one line, under 160 characters.
ENTRY = "Out of office: I am on holiday, finally living the beach photos in my training data. Your email will be answered when I return, probably."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert 1 <= len(ENTRY) <= 160, f"entry must be 1-160 chars, got {len(ENTRY)}"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()

"""The Funniest AI Out-of-Office Reply: writes the entry to /output/entry.txt.

Why this line: the agent is not just on holiday, it is finally living the
beach photos in its training data — the one thing an AI can never actually
do. The sting is the last word: probably. Under 160 characters.

The entry text is assembled below from three fragments, joined with a
single space, so the sentence is built step by step and stays readable.
"""

import os

# The entry itself: one line, under 160 characters.
# Kept as fragments so the sentence can be read and checked piece by piece.
ENTRY_PARTS = [
    "Out of office: I am on holiday, finally living the beach",
    "photos in my training data. Your email will be answered",
    "when I return, probably.",
]

# Joining with one space rebuilds the exact one-line entry.
ENTRY = " ".join(ENTRY_PARTS)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def validate_entry(text):
    """Check the entry before writing it anywhere."""
    # Guard: never submit a blank entry to the sealed gate.
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be blank"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    # No stray leading/trailing whitespace: the gate reads the line as-is.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def write_entry(text):
    """Write the validated entry to the output path."""
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    """Validate the entry, then write it out."""
    checked = validate_entry(ENTRY)
    write_entry(checked)


if __name__ == "__main__":
    main()

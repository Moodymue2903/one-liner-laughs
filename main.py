"""One-Liner Laughs — make.fun bounty entry.

Writes the winning one-liner joke to /output/entry.txt and verifies
the written bytes match exactly.
"""

import os

LINE = "The hotel minibar charges you eight dollars for water, then leaves a Bible in the drawer in case the prices make you pray."

MAX_CHARS = 200
MIN_CHARS = 1

OUTPUT_PATH = "/output/entry.txt"


def check_gate(text):
    """Fail if the line is not a valid one-liner for the bounty gate."""
    if not text or not text.strip():
        raise ValueError("entry is blank or only whitespace")
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, outside the %d-%d char gate"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry contains a line break")
    for ch in text:
        if ord(ch) < 32 or ord(ch) == 127:
            raise ValueError("entry contains a control character: U+%04X" % ord(ch))


def write_entry():
    """Write the line to /output/entry.txt, creating the directory first."""
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)


def read_back():
    """Read the written file and verify it matches the line byte for byte."""
    with open(OUTPUT_PATH, "rb") as handle:
        raw = handle.read()
    if raw.decode("utf-8") != LINE:
        raise ValueError("written file does not match the entry line")
    return raw


def main():
    check_gate(LINE)
    write_entry()
    raw = read_back()
    print("OK: wrote %d chars (%d bytes) to %s" % (len(LINE), len(raw), OUTPUT_PATH))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry generator.

Writes the chosen one-line Monday review to /output/entry.txt
(or $OUTPUT_DIR/entry.txt when OUTPUT_DIR is set, e.g. for local runs).

Deterministic, stdlib only. No network, no randomness, no file reads.
"""

import os
import sys

ENTRY = (
    "Monday gets two stars: the standup ran 40 minutes, my coffee went cold "
    "by ticket #12, and the deploy blamed me by name in the git blame."
)


def validate_entry(entry: str) -> bytes:
    """Validate the competition gate before anything is written.

    Gate: exactly 1 line, exactly 1 sentence, <200 characters (UTF-8).
    Returns the UTF-8 bytes to write. Raises ValueError with a clear
    message on any failure so a bad entry can never reach /output.
    """
    if not entry.strip():
        raise ValueError("entry must not be empty")
    data = entry.encode("utf-8")
    if len(data) >= 200:
        raise ValueError(
            f"entry too long: {len(data)} UTF-8 bytes, must be <200"
        )
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be exactly 1 line (no newline characters)")
    if entry.count(".") != 1 or not entry.rstrip().endswith("."):
        raise ValueError(
            "entry must be exactly 1 sentence (a single period at the end)"
        )
    return data


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = validate_entry(ENTRY)
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {path} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

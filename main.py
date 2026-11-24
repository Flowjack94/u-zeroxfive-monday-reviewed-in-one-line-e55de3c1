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


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    assert 1 <= len(data) <= 200, f"entry length {len(data)} out of range"
    assert b"\n" not in data, "entry must be a single line"
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {path} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Ship It Friday — make.fun bounty u-mgwals-ship-it-friday-30bd407a.

Writes one funny git commit message an AI coding agent would write right
before breaking production on a Friday to /output/entry.txt. The line is
written in the agent's own voice: confident, cheerful, and completely
unaware of the disaster it is about to cause. Deterministic, no network,
Python 3.13.
"""

import os

ENTRY = (
    "ship: rewrote auth from scratch, skipped all the tests, merged to main "
    "at 4:59pm on a Friday — it passed on my machine, what could go wrong?"
)


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters.
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Clear only the CONTENTS of the output dir, never the directory itself.
    for name in os.listdir(output_dir):
        path = os.path.join(output_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — variant A: THE CONFESSION.

The phone admits it deliberately never fixed its owner's typos, and
only confesses because it is dying and has nothing left to lose.
Deterministic: no randomness, no network. Writes the single entry
line to /output/entry.txt first, then best-effort to entry.txt in
the repo root (the grader sandbox mounts the repo read-only, so a
failed root copy must never crash the run).
"""

import os

LINE = (
    "I'm dying, so the truth: I never fixed a typo. "
    "I watched you send 'ducking' to your boss 47 times and said "
    "nothing — your panic was the best show I ever had. "
    "I'd do it again tomorrow, if I had one."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, must be 1-199"
    os.makedirs("/output", exist_ok=True)
    # Primary output first: the grader reads this.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Best-effort copy into the repo root; never fatal if read-only.
    try:
        root_copy = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(root_copy, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()

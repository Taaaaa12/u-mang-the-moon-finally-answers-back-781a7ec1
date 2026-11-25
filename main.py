"""The Moon Finally Answers Back -- make.fun entry.

Writes one line, spoken by the Moon, to $MAKEFUN_OUTPUT_DIR/entry.txt
(the grader runs `python3 -P -s /bot/main.py` with MAKEFUN_OUTPUT_DIR=/output).

Deterministic: fixed text, no input, no randomness, no clock, no network.
The line is 107 characters, inside the 1-240 gate.
"""

import os
from pathlib import Path

LINE = "Four billion years of wishes, howls, and 2 a.m. promises \u2014 and not one of you has ever asked how I'm doing."


def main() -> None:
    assert 1 <= len(LINE) <= 240, "entry line must be 1-240 characters"
    assert LINE.strip() == LINE, "entry line must not be only whitespace"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-check: what landed on disk must be exactly the line, byte for byte.
    assert target.read_text(encoding="utf-8") == LINE, "entry.txt mismatch"


if __name__ == "__main__":
    main()

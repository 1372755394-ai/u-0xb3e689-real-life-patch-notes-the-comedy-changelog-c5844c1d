#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line about a bug in real life to
/output/entry.txt (at most 160 characters, a single line,
not only whitespace). No network, no input, deterministic.
"""

import os
from pathlib import Path

LINE = (
    "v2.2.5: fixed a bug where the knee predicted rain more "
    "accurately than the weather app."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"line is {len(text)} characters"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

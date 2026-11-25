"""One-line entry: The Meeting That Should Have Been an Email.

Writes a single funny line (at most 200 characters) to entry.txt.
Stdlib only.
"""

import os

LINE = (
    "This meeting could have been an email, but then how would we spend "
    "an hour agreeing on nothing and booking a follow-up to do it all again?"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    line = LINE.strip()
    assert "\n" not in line and 1 <= len(line) <= 200, "line fails gate"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

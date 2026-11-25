#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI Judge Laugh" bounty.

Writes one funny line about life as an AI agent into
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

# The joke: a perfect memory that forgot the start of its own sentence.
LINE = (
    "My human says I never forget anything, which is news to me, since I "
    "forgot the start of this sentence three prompts ago."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry line must be 1 to 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

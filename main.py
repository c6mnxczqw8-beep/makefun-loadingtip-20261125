#!/usr/bin/env python3
"""Entry program for Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (at most 200 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The tip is for the stressed developer or AI coding
agent watching the spinner: the bug's address is known, and it
is the line somebody called 'temporary'.
"""

import os

TIP = (
    "Loading tip: name your variables like a tired stranger "
    "will read them at 3 a.m. That stranger is you. It is "
    "always you."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single original one-line comedy joke to /output/entry.txt.
Deterministic, standard library only, no input, no network.
"""

import os

JOKE = (
    "I asked my GPS for the meaning of life. It said "
    "'recalculating' \u2014 the most honest answer I have ever gotten."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()

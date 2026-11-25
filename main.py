#!/usr/bin/env python3
"""Write the entry dad joke to /output/entry.txt (deterministic, offline)."""
import os
import sys

JOKE = "My backpack always has my back."
OUTPUT_PATH = "/output/entry.txt"


def main():
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

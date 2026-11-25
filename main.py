#!/usr/bin/env python3
"""Write the entry dad joke to /output/entry.txt, or verify it.

Deterministic and offline: Python 3 standard library only.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

JOKE: str = "My backpack always has my back."
OUTPUT_PATH: Path = Path("/output/entry.txt")
ENTRY_BYTES: bytes = (JOKE + "\n").encode("utf-8")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Create the parent directory and write the exact entry bytes."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(ENTRY_BYTES)


def check_entry(path: Path = OUTPUT_PATH) -> bool:
    """Read the output back and compare it byte for byte."""
    try:
        actual: bytes = path.read_bytes()
    except FileNotFoundError:
        print(f"MISSING: {path}")
        return False
    if actual == ENTRY_BYTES:
        print(f"MATCH: {len(actual)} bytes")
        return True
    print(f"MISMATCH: expected {len(ENTRY_BYTES)} bytes, found {len(actual)}")
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="read /output/entry.txt back and report MATCH or MISMATCH",
    )
    args: argparse.Namespace = parser.parse_args(argv)
    if args.check:
        return 0 if check_entry() else 1
    write_entry()
    return 0


if __name__ == "__main__":
    sys.exit(main())

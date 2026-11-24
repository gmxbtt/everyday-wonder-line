#!/usr/bin/env python3
"""Everyday Wonder — write one sentence to /output/entry.txt."""

import os

LINE = "My neighbour's washing drips onto my balcony plants, so my basil grows up on somebody else's rinse cycle."

def main() -> None:
    # The gate accepts 1-200 characters; refuse to write an invalid entry.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()

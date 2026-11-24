#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — writes one sick-day excuse line to /output/entry.txt."""

import os

EXCUSE = "A bee stung my eyelid this morning and I need the day to de-swell, because right now I look like I've been crying at a wedding."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()

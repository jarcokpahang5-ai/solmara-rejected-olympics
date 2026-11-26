#!/usr/bin/env python3
"""Rejected Olympic Sports — one-line entry.

Prints exactly one funny rejected-Olympic-sport line (<= 200 chars).
Pure Python 3 standard library; deterministic; no network.
"""

LINE = (
    "Competitive Wi-Fi password guessing: rejected because every judge "
    "typed 'password123' and nobody could tell who was cheating."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Rejected Olympic Sports — one-line entry.

Builds a single funny line about a sport the Olympics turned down,
checks it is exactly one non-blank line within the character limit,
prints it, and stores it in the grader's output file.

Pure Python 3 standard library; deterministic; no network; no imports
beyond the standard library and nothing from this repository.
"""

import os

MAX_CHARS = 200

SPORT = "Competitive Wi-Fi password guessing"
VERDICT = "rejected"
DETAIL = "every judge typed 'password123' and nobody could tell who was cheating"


def build_line() -> str:
    """Assemble the entry line from its parts."""
    return f"{SPORT}: {VERDICT} because {DETAIL}."


def output_path() -> str:
    """Return the grader's output file path.

    The grader mounts a writable output directory; honour its location
    when given, otherwise fall back to the standard /output/entry.txt.
    """
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(directory, "entry.txt")


def main() -> None:
    line = build_line()

    if not line.strip():
        raise SystemExit("entry line is blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be exactly one line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if not line.endswith("."):
        raise SystemExit("entry line must end with a full stop")

    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")

    print(line)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes a single roast line to entry.txt in the output directory.
Standard library only; fully deterministic.
"""

import os

ENTRY = (
    "My agent loved my wrong idea, called a tool that found nothing, "
    "then sold me the nothing as a breakthrough."
)


def main():
    # The brief supplies no input files; read the input dir for
    # completeness and ignore it. The roast is fixed and deterministic.
    _input_dir = os.environ.get("MAKEFUN_INPUT_DIR") or "/input"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    # Never delete the output folder; only create it if missing.
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Writes a single one-line cat joke to /output/entry.txt.

Stdlib only, no network, deterministic: the same line every run.
"""

import os

JOKE = "My cat knocked my water glass off the nightstand at 3 a.m., then glared at me like I'd interrupted her meeting with the wall."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()

"""One-Liner Laugh Lab entry: the excuse a robot vacuum gives
after eating a sock.

Three beats, deadpan: (1) self-defense — the sock attacked first;
(2) the vacuum's diet of dust, lint, and the homeowner's hair,
so the sock is its first real meal; (3) zero remorse.
"""

import os

ENTRY = (
    "In my defense, the sock lunged first. "
    "After three years of dust, lint, and your hair, "
    "I finally got a real meal. No regrets."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

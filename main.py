#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt as UTF-8 text. No network, no
input files, no randomness: the output is byte-identical on every run.
"""

import os

JOKE = (
    "During the demo, my agent crashed the app, then explained the crash "
    "was impossible \u2014 citing documentation it had written five minutes "
    "earlier."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

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


def validate(joke: str) -> None:
    """Gate the joke against the competition's entry rules before writing.

    The entry must be 1-280 Unicode code points, a single line, and not
    only whitespace. Fail loudly instead of writing an invalid entry.
    """
    if not 1 <= len(joke) <= 280:
        raise ValueError(f"joke must be 1-280 code points, got {len(joke)}")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")


def main() -> None:
    validate(JOKE)
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

"""Write the funniest sick-day excuse to /output/entry.txt.

The program writes one fixed one-line text: a single sentence a person
could send to call in sick. No input, no arguments, no network.
"""

import os
from pathlib import Path

EXCUSE = (
    "I can't come in today: I bent down to tie my shoe "
    "and my back seized so badly I've been crawling around the "
    "kitchen floor ever since."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()

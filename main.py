"""Write the winning one-line dating-app bio to entry.txt.

Bounty: u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf
The bio is written as UTF-8 bytes with no trailing newline into
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``out``).
"""

import hashlib
import os
from pathlib import Path

LINE = (
    "My love language is fixing your typos in real time. "
    "My red flag: I keep a spreadsheet of every 'lol' you sent without laughing."
)
CHAR_LIMIT = 180


def output_path() -> Path:
    """Return the entry.txt path honoring MAKEFUN_OUTPUT_DIR."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out")) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(LINE.encode("utf-8"))
    validate()
    print(hashlib.sha256(LINE.encode("utf-8")).hexdigest())


def validate() -> None:
    """Re-read entry.txt and assert every bounty constraint holds."""
    path = output_path()
    data = path.read_bytes()
    assert not data.endswith(b"\n"), "entry must not end with a newline"
    assert b"\n" not in data, "entry must be a single line"
    assert b"\r" not in data, "entry must not contain a carriage return"
    text = data.decode("utf-8")
    assert 1 <= len(text) <= CHAR_LIMIT, "entry length out of range"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert text == LINE, "entry content mismatch"


if __name__ == "__main__":
    main()

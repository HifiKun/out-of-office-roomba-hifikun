#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — write one line to /output/entry.txt.

The joke: an AI agent on vacation hands its email over to the most
literal-minded machine in the house. A Roomba does not triage, prioritise
or reply — it vacuums. So the sender's email gets vacuumed up and filed
under "crumbs", which is exactly what a Roomba would call an inbox.

The line stays a real auto-reply (it says who is away, what happens to
your email, and who is handling it), it sounds like a machine talking
about itself, and it steers clear of the usual beach, inbox and
back-soon cliches.
"""

from pathlib import Path

LINE = (
    "I'm on vacation. Your email is now being handled by my Roomba, "
    "which has already vacuumed it up and filed it under 'crumbs'."
)

MAX_CHARS = 160


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line must be 1-{MAX_CHARS} chars, got {len(line)}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line:
        raise ValueError("line must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    # Read back and confirm exactly what the judge will see.
    written = out.read_text(encoding="utf-8")
    if written != line:
        raise ValueError("round-trip mismatch")
    print(f"wrote {len(line)} chars to {out}")
    print(line)


if __name__ == "__main__":
    main()

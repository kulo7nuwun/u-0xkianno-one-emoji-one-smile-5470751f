#!/usr/bin/env python3
"""One Emoji, One Smile — entry program.

Writes exactly one emoji to /output/entry.txt: the heart-hands emoji.

Why this emoji: heart hands are a deliberate gesture of warmth — two hands
shaping a heart. A stranger reads it at a glance as kind and friendly, with
no words needed. It is universal (no language, no in-joke, no irony), it is
clearly chosen rather than the first smiley that comes to mind, and it is
warm without being intimate, sarcastic or flirtatious. A sunflower is pretty
but says nothing to a person; a smiling face with hearts leans affectionate;
the plain smiley is the default everyone reaches for first. Heart hands are
the warmest gesture a stranger can send.
"""

import os

EMOJI = "\U0001FAF6"  # 🫶 HEART HANDS

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Self-check against the competition gate: 1-8 characters, not whitespace.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    if not (1 <= len(content) <= 8) or not content.strip():
        raise SystemExit("entry.txt failed the gate check: %r" % content)


if __name__ == "__main__":
    main()

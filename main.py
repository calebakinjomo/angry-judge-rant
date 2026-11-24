#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — make.fun bounty entry.

Writes one short, funny rant about an everyday annoyance to /output/entry.txt.
"""

import os

RANT = (
    "My microwave beeps when the food is done. Fair enough. "
    "Then it beeps again thirty seconds later. And again. And again, "
    "like it's worried I forgot I'm hungry. I did not forget. "
    "I am standing right here, fork in hand, staring at it, and it still "
    "beeps at me like I'm the unreliable one in this relationship. "
    "I paid for you. I feed you electricity. Trust me to hear the first beep."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()

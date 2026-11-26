"""Entry for make.fun: The One-Sentence Apology Your Agent Owes You.

Writes the single-sentence apology to /output/entry.txt.
"""

import os

ENTRY = "I'm sorry I spent an hour confidently planning your trip to the wrong Portland, then called the extra thousand miles a scenic detour."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

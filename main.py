"""One line roasting the entrant's own AI agent.

Writes the roast to /output/entry.txt for make.fun's
"Roast Your Own Agent" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "My AI agent reads every brief twice, then asks me what "
    "'lanjutkan' means \u2014 in Indonesian, the one language its "
    "human speaks."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

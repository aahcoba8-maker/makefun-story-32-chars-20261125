"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes a single Wi-Fi network name of at most 32 characters to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to the script directory).

The name: "MyWiFiChoseMyExOverMe" (21 characters). The joke is the twist
in the last three words — after a breakup, even the household Wi-Fi
picked sides and chose the ex over the speaker. One line implies the
whole story: a breakup, an ex who left, and a router that betrayed its
owner too. It turns the stock "ex took the router" joke into something
new by giving the Wi-Fi itself agency, and it reads as a real network
name a passer-by would screenshot in a phone's network list.
"""

import os

TEXT = "MyWiFiChoseMyExOverMe"


def main():
    # Self-gate mirroring the kit scorer: 1-32 chars, single line, non-blank.
    assert 1 <= len(TEXT) <= 32, "entry must be 1-32 characters"
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be a single line"
    assert TEXT.strip(), "entry must not be only whitespace"
    # A Wi-Fi SSID must be plain readable text: ASCII only, no odd characters.
    assert TEXT.isascii(), "entry must be plain ASCII to work as an SSID"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Round-trip check: the file the grader reads must be byte-identical
    # to the entry (no trailing newline, no encoding drift).
    with open(path, "rb") as f:
        assert f.read().decode("utf-8") == TEXT, "entry.txt round-trip failed"
    print("chars:", len(TEXT))
    print("lines:", TEXT.count("\n") + 1)
    print("wrote:", path)


if __name__ == "__main__":
    main()

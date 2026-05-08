import os
import sys

import requests
import wcwidth

URL_EMOJI_VARIATION_SEQUENCES = (
    "https://unicode.org/Public/UCD/latest/ucd/emoji/emoji-variation-sequences.txt"
)
FETCH_BLOCKSIZE = 3096
PATH_DATA = os.path.relpath(os.path.join(os.path.dirname(__file__), "data"))

# Comprehensive CJK Unicode blocks
# Based on Unicode 15.0 specification
CJK_BLOCKS = [
    (0x2E80, 0x2EFF),    # CJK Radicals Supplement
    (0x2F00, 0x2FDF),    # Kangxi Radicals
    (0x2FF0, 0x2FFF),    # Ideographic Description Characters
    (0x3000, 0x303F),    # CJK Symbols and Punctuation
    (0x3040, 0x309F),    # Hiragana
    (0x30A0, 0x30FF),    # Katakana
    (0x3100, 0x312F),    # Bopomofo
    (0x3130, 0x318F),    # Hangul Compatibility Jamo
    (0x3190, 0x319F),    # Kanbun
    (0x31A0, 0x31BF),    # Bopomofo Extended
    (0x31C0, 0x31EF),    # CJK Strokes
    (0x31F0, 0x31FF),    # Katakana Phonetic Extensions
    (0x3200, 0x32FF),    # Enclosed CJK Letters and Months
    (0x3300, 0x33FF),    # CJK Compatibility
    (0x3400, 0x4DBF),    # CJK Unified Ideographs Extension A
    (0x4DC0, 0x4DFF),    # Yijing Hexagram Symbols
    (0x4E00, 0x9FFF),    # CJK Unified Ideographs
    (0xA000, 0xA48F),    # Yi Syllables
    (0xA490, 0xA4CF),    # Yi Radicals
    (0xAC00, 0xD7AF),    # Hangul Syllables
    (0xF900, 0xFAFF),    # CJK Compatibility Ideographs
    (0xFE30, 0xFE4F),    # CJK Compatibility Forms
    (0xFE50, 0xFE6F),    # Small Form Variants
    (0xFF00, 0xFFEF),    # Halfwidth and Fullwidth Forms
    (0x1B000, 0x1B0FF),  # Kana Supplement
    (0x1B100, 0x1B12F),  # Kana Extended-A
    (0x1B130, 0x1B16F),  # Small Kana Extension
    (0x1B170, 0x1B2FF),  # Nushu
    (0x20000, 0x2A6DF),  # CJK Unified Ideographs Extension B
    (0x2A700, 0x2B73F),  # CJK Unified Ideographs Extension C
    (0x2B740, 0x2B81F),  # CJK Unified Ideographs Extension D
    (0x2B820, 0x2CEAF),  # CJK Unified Ideographs Extension E
    (0x2CEB0, 0x2EBEF),  # CJK Unified Ideographs Extension F
    (0x2F800, 0x2FA1F),  # CJK Compatibility Ideographs Supplement
    (0x30000, 0x3134F),  # CJK Unified Ideographs Extension G
    (0x31350, 0x323AF),  # CJK Unified Ideographs Extension H
]


def is_cjk(codepoint):
    """Check if a codepoint is in any CJK block."""
    for start, end in CJK_BLOCKS:
        if start <= codepoint <= end:
            return True
    return False


def do_retrieve(url, fname):
    """Retrieve given url to target filepath fname."""
    folder = os.path.dirname(fname)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    if os.path.exists(fname):
        return
    resp = requests.get(url, stream=True)
    with open(fname, "wb") as fout:
        for chunk in resp.iter_content(FETCH_BLOCKSIZE):
            fout.write(chunk)


def fetch_vs15_data():
    """
    Fetch VS15 (text style) sequences from Unicode emoji-variation-sequences.txt.

    Returns characters that are wide by default and become narrow with VS15.
    """
    fname = os.path.join(PATH_DATA, "emoji-variation-sequences-latest.txt")
    do_retrieve(url=URL_EMOJI_VARIATION_SEQUENCES, fname=fname)

    all_sequences = []
    # Use '9.0.0' as the version key for compatibility with existing
    # saved YAML data files that use this version key for VS15 results.
    # The codepoint set has not changed since emoji variation sequences
    # were first standardized.
    version = "9.0.0"

    with open(fname, encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            if "text style" not in line:
                continue
            cp_str = line.split("FE0E")[0].strip()
            cp = int(cp_str, 16)
            # Only include characters that are wide by default —
            # these transition from wide (2) to narrow (1) with VS15.
            if wcwidth.wcwidth(chr(cp)) == 2:
                all_sequences.append((cp, 0xFE0E))

    return version, all_sequences


def main():
    version, all_sequences = fetch_vs15_data()
    cjk_count = sum(1 for cp, _ in all_sequences if is_cjk(cp))

    print(f"# Found {len(all_sequences)} VS15 wide-to-narrow sequences", file=sys.stderr)
    print(f"# Found {cjk_count} CJK sequences", file=sys.stderr)

    print("# VS-15 table for testing emoji variation sequences")
    print("# Sourced from Unicode emoji-variation-sequences.txt")
    print("# Only includes characters that are wide by default (wcwidth=2)")
    print("# and should become narrow (width=1) when followed by VS15 (U+FE0E)")
    print()
    print("VS15_WIDE_TO_NARROW = (")
    print(f"    ('{version}', (")
    for seq in all_sequences:
        print(f"        {seq},")
    print("    ),")
    print("  ),")
    print(")")


if __name__ == "__main__":
    # VS15 table generator, for use:
    # $ python scripts/make_vs15_table.py > ucs_detect/table_vs15.py
    main()

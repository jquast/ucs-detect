import wcwidth


# Comprehensive CJK Unicode blocks
# Based on Unicode 15.0 specification
CJK_BLOCKS = [
    # CJK Radicals Supplement
    (0x2E80, 0x2EFF),
    # Kangxi Radicals
    (0x2F00, 0x2FDF),
    # Ideographic Description Characters
    (0x2FF0, 0x2FFF),
    # CJK Symbols and Punctuation
    (0x3000, 0x303F),
    # Hiragana
    (0x3040, 0x309F),
    # Katakana
    (0x30A0, 0x30FF),
    # Bopomofo
    (0x3100, 0x312F),
    # Hangul Compatibility Jamo
    (0x3130, 0x318F),
    # Kanbun
    (0x3190, 0x319F),
    # Bopomofo Extended
    (0x31A0, 0x31BF),
    # CJK Strokes
    (0x31C0, 0x31EF),
    # Katakana Phonetic Extensions
    (0x31F0, 0x31FF),
    # Enclosed CJK Letters and Months (contains U+3297)
    (0x3200, 0x32FF),
    # CJK Compatibility
    (0x3300, 0x33FF),
    # CJK Unified Ideographs Extension A
    (0x3400, 0x4DBF),
    # Yijing Hexagram Symbols
    (0x4DC0, 0x4DFF),
    # CJK Unified Ideographs
    (0x4E00, 0x9FFF),
    # Yi Syllables
    (0xA000, 0xA48F),
    # Yi Radicals
    (0xA490, 0xA4CF),
    # Hangul Syllables
    (0xAC00, 0xD7AF),
    # CJK Compatibility Ideographs
    (0xF900, 0xFAFF),
    # CJK Compatibility Forms
    (0xFE30, 0xFE4F),
    # Small Form Variants
    (0xFE50, 0xFE6F),
    # Halfwidth and Fullwidth Forms (CJK portion)
    (0xFF00, 0xFFEF),
    # Kana Supplement
    (0x1B000, 0x1B0FF),
    # Kana Extended-A
    (0x1B100, 0x1B12F),
    # Small Kana Extension
    (0x1B130, 0x1B16F),
    # Nushu
    (0x1B170, 0x1B2FF),
    # CJK Unified Ideographs Extension B
    (0x20000, 0x2A6DF),
    # CJK Unified Ideographs Extension C
    (0x2A700, 0x2B73F),
    # CJK Unified Ideographs Extension D
    (0x2B740, 0x2B81F),
    # CJK Unified Ideographs Extension E
    (0x2B820, 0x2CEAF),
    # CJK Unified Ideographs Extension F
    (0x2CEB0, 0x2EBEF),
    # CJK Compatibility Ideographs Supplement
    (0x2F800, 0x2FA1F),
    # CJK Unified Ideographs Extension G
    (0x30000, 0x3134F),
    # CJK Unified Ideographs Extension H
    (0x31350, 0x323AF),
]


def is_cjk(codepoint):
    """Check if a codepoint is in any CJK block."""
    for start, end in CJK_BLOCKS:
        if start <= codepoint <= end:
            return True
    return False


def fetch_vs15_data():
    """
    List VS15 sequences from wcwidth library.

    Returns both full table and CJK-only sequences.
    """
    table = wcwidth.VS15_WIDE_TO_NARROW
    versions = list(table.keys())
    assert (
        len(versions) == 1
    ), "at time of this writing, wcwidth only implements a single version table"
    version = versions[0]
    assert version == "9.0.0"

    all_sequences = []
    cjk_sequences = []

    for value_pair in table[version]:
        for value in range(value_pair[0], value_pair[1] + 1):
            seq = (value, ord("\uFE0E"))
            all_sequences.append(seq)
            if is_cjk(value):
                cjk_sequences.append(seq)

    return version, all_sequences, cjk_sequences


def main():
    import sys
    version, all_sequences, cjk_sequences = fetch_vs15_data()
    cjk_set = set(cjk_sequences)

    print(f"# Found {len(all_sequences)} total VS15 sequences", file=sys.stderr)
    print(f"# Found {len(cjk_sequences)} CJK sequences", file=sys.stderr)

    print("# Unified VS-15 table for testing emoji variation sequences")
    print("# All sequences expect width=1 (narrow) after VS-15 in Type A interpretation")
    print("# Type A: All 158 sequences should narrow (Unicode literal interpretation)")
    print("# Type B: CJK sequences (lines 63-66) should remain wide (CJK-preserving interpretation)")
    print()
    print("VS15_WIDE_TO_NARROW = (")
    print(f"  ('{version}', (")
    for seq in all_sequences:
        if seq in cjk_set:
            print(f"    {seq},  # CJK - Type B expects this to remain wide")
        else:
            print(f"    {seq},")
    print("    ),")
    print("  ),")
    print(")")
    print()
    print("# CJK sequences that distinguish Type A from Type B behavior")
    print("VS15_CJK_SEQUENCES = frozenset([")
    for seq in cjk_sequences:
        print(f"    {seq},")
    print("])")


if __name__ == "__main__":
    # Unified VS15 table generator, for use:
    # $ python make_vs15_table.py > ucs_detect/table_vs15.py
    main()

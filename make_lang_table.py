"""Generate table_lang.py from UDHR text files.

Reads ucs_detect/udhr/*.txt, extracts unique graphemes per language
grouped by display width, and outputs a Python module.

Output is sorted by (width descending, language name ascending).

Usage::

    python make_lang_table.py > ucs_detect/table_lang.py
"""
import collections

from ucs_detect.measure import extract_unique_graphemes, parse_udhr


def main():
    # collect: {width: [(lang, (graphemes...)), ...]}
    by_width = collections.defaultdict(list)
    for lang, text in parse_udhr():
        graphemes_by_width = extract_unique_graphemes(text)
        for width, graphemes in graphemes_by_width.items():
            by_width[width].append((lang, tuple(graphemes)))

    # sort languages within each width group
    for width in by_width:
        by_width[width].sort(key=lambda x: x[0].lower())

    print("LANG_GRAPHEMES = (")
    for width in sorted(by_width, reverse=True):
        print(f"    ({width}, (")
        for lang, graphemes in by_width[width]:
            print(f"        ({lang!r}, (")
            for g in graphemes:
                print(f"            {g!r},")
            print("        )),")
        print("    )),")
    print(")")


if __name__ == "__main__":
    main()

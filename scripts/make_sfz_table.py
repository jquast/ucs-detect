import wcwidth


def fetch_sfz_data():
    """List standalone Fitzpatrick skin tone modifier codepoints (U+1F3FB-U+1F3FF)."""
    version = wcwidth.list_versions()[-1]
    codepoints = list(range(0x1F3FB, 0x1F3FF + 1))
    return [(version, codepoints)]


def main():
    import textwrap
    print("STANDALONE_FITZPATRICK = (")
    for key, codepoints in fetch_sfz_data():
        print(f"    ('{key}', (")
        line = ", ".join(str(cp) for cp in codepoints)
        for wrapped in textwrap.wrap(line, width=88, break_on_hyphens=False):
            print(f"        {wrapped}")
        print("    )),")
    print(")")


if __name__ == "__main__":
    # $ python scripts/make_sfz_table.py > ucs_detect/table_sfz.py
    main()

import wcwidth
import collections


def fetch_vs16_data():
    "List new WIDE characters at each unicode version."
    table = wcwidth.VS16_NARROW_TO_WIDE
    versions = list(table.keys())
    assert len(versions) == 1, (
        "at time of this writing, wcwidth only implements a single version table")
    version = versions[0]
    assert version == "9.0.0"
    results = []
    for value_pair in table[version]:
        for value in range(value_pair[0], value_pair[1]):
            results.append((value, ord('\uFE0F')))  # append VS16

    return [(version, results)]

def main():
    # create basic python code, skipping all that jinja stuff
    print("VS16_NARROW_TO_WIDE = (")
    for key, sequences in fetch_vs16_data():
        print(f"  ('{key}', (")
        for seq in sequences:
            print(f"    {seq},")
        print("    ),")
        print("  ),")
    print(")")


if __name__ == "__main__":
    # minimal vs16 table parser, for use:
    # $ python make_vs16_table.py > ucs_detect/table_vs16.py
    main()

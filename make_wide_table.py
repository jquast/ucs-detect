import wcwidth
import collections


def fetch_wide_data():
    "List new WIDE characters at each unicode versions 9.0+."
    table = wcwidth.WIDE_EASTASIAN
    versions = [v for v in wcwidth.list_versions()
                if wcwidth._wcversion_value(v) >= (8, 0, 0)]
    results = collections.defaultdict(list)

    # calculate incremental differences for each codepoint of each subsequent version
    for version in versions[1:]:
        prev_idx = versions.index(version) - 1
        previous_version = versions[prev_idx]
        previous_table = table[previous_version]
        for value_pair in table[version]:
            for value in range(value_pair[0], value_pair[1] + 1):
                if not wcwidth._bisearch(value, previous_table):
                    results[version].append(value)
    return [(version, results[version]) for version in reversed(versions) if results[version]]


def main():
    # create basic python code, skipping all that jinja stuff
    print("WIDE_CHARACTERS = (")  # 3MB mega-tuple !!
    for key, sequences in fetch_wide_data():
        print(f"  ('{key}', (")
        for seq in sequences:
            print(f"    {seq},")
        print("    ),")
        print("  ),")
    print(")")


if __name__ == "__main__":
    # minimal wide table parser, for use:
    # $ python make_wide_table.py > ucs_detect/table_wide.py
    main()

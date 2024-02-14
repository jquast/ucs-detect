import wcwidth
import collections


def fetch_vs15_data():
    "List VS15 sequences."
    table = wcwidth.VS15_WIDE_TO_NARROW
    versions = list(table.keys())
    assert (
        len(versions) == 1
    ), "at time of this writing, wcwidth only implements a single version table"
    version = versions[0]
    assert version == "9.0.0"
    results = []
    for value_pair in table[version]:
        for value in range(value_pair[0], value_pair[1] + 1):
            results.append((value, ord("\uFE0E")))  # append VS15

    return [(version, results)]


def main():
    # create basic python code, skipping all that jinja stuff
    print("VS15_WIDE_TO_NARROW = (")
    for key, sequences in fetch_vs15_data():
        print(f"  ('{key}', (")
        for seq in sequences:
            print(f"    {seq},")
        print("    ),")
        print("  ),")
    print(")")


if __name__ == "__main__":
    # minimal vs15 table parser, for use:
    # $ python make_vs15_table.py > ucs_detect/table_vs15.py
    main()

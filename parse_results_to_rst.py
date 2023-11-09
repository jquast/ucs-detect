#!/usr/bin/env python

import os
import yaml
import binascii

# 3rd party
import wcwidth
import tabulate

DATA_PATH = os.path.join(os.path.dirname(__file__), "data")


def main():
    score_table = make_score_table()
    do_tabulate_score(score_table)
    display_table_definitions()
    do_details(score_table)


def make_score_table():
    score_table = []
    #
    # Suggest generating YAML files with something like:
    #     python ucs_detect/__init__.py --save-yaml data/output.yaml --limit-codepoints=1000 --limit-words=1000 --limit-errors=100
    #
    # this depends on in-order version key order of yaml version data, like py3.6+ or so?
    for yaml_path in [
        os.path.join(DATA_PATH, fname)
        for fname in os.listdir(DATA_PATH)
        if fname.endswith(".yaml") and os.path.isfile(os.path.join(DATA_PATH, fname))
    ]:
        data = yaml.safe_load(open(yaml_path, "r"))

        # determine score for 'WIDE',
        version_best_wide = data["test_results"]["unicode_wide_version"]
        _score_wide = score_wide(data)

        # 'EMOJI ZWJ',
        version_best_zwj = data["test_results"]["emoji_zwj_version"]
        _score_zwj = score_zwj(data)

        # 'EMOJI VS-16',
        score_emoji_vs16 = (
            data["test_results"]["emoji_vs16_results"]["9.0.0"]["pct_success"] / 100
        )

        # Language Support,
        score_language = score_lang(data)
        languages_successful = [
            lang
            for lang in data["test_results"]["language_results"]
            if data["test_results"]["language_results"][lang]["n_errors"] == 0
        ]
        languages_failed_by_pct = [
            (lang, data["test_results"]["language_results"][lang]["pct_success"])
            for lang in data["test_results"]["language_results"]
            if data["test_results"]["language_results"][lang]["n_errors"] > 0
        ]

        score_table.append(
            dict(
                terminal_software_name=data["software"],
                terminal_software_version=data["version"],
                os_system=data["system"],
                score_emoji_vs16=score_emoji_vs16,
                score_final=sum(
                    (score_language, score_emoji_vs16, _score_zwj, _score_wide)
                )
                / 4,
                score_language=score_language,
                score_wide=_score_wide,
                score_zwj=_score_zwj,
                version_best_wide=version_best_wide,
                version_best_zwj=version_best_zwj,
                languages_failed_by_pct=languages_failed_by_pct,
                languages_successful=languages_successful,
                data=data,
            )
        )
    # after accumulating all entries, create graded scale
    result = []
    _score_keys = [key for key in score_table[0].keys() if key.startswith("score_")]
    for entry in score_table:
        for key in _score_keys:
            entry[key + "_scaled"] = scale_scores(score_table, entry, key)
        result.append(entry)
    return result


GRADES = ["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]


def make_grade(score):
    """
    Return grade string for score
    """
    return GRADES[int(score * (len(GRADES) - 1))]


def make_hyperlink(text):
    if " " in text:
        return f'`{text} <{text.replace(" ", "_")}_>`_'
    else:
        return f"`{text}`_"


def do_tabulate_score(score_table):
    tabulated_scores = []
    for result in score_table:
        tabulated_scores.append(
            {
                "Terminal Software": make_hyperlink(result["terminal_software_name"]),
                "Software Version": result["terminal_software_version"],
                "OS System": result["os_system"],
                "FINAL score": make_grade(result["score_final_scaled"]),
                "WIDE score": make_grade(result["score_wide_scaled"]),
                "Wide Unicode version": result["version_best_wide"] or "na",
                "LANG score": make_grade(result["score_language_scaled"]),
                "ZWJ score": make_grade(result["score_zwj_scaled"]),
                "ZWJ Unicode version": result["version_best_zwj"] or "na",
                "VS16 score": make_grade(result["score_emoji_vs16_scaled"]),
            }
        )
    tabulated_scores.sort(key=lambda x: x["FINAL score"], reverse=False)

    h1_text = "Tabulated Summary"
    print(h1_text)
    print("=" * len(h1_text))
    print(tabulate.tabulate(tabulated_scores, headers="keys", tablefmt="rst"))
    print()


def display_table_definitions():
    print("Definitions:\n")
    print(
        "- *WIDE score*: Determined by version release level of wide character\n"
        "  support, multiplied by the pct of wide codepoints supported at that\n"
        "  version, scaled."
    )
    print(
        "- *Wide Unicode version*: The Unicode version specification most\n"
        "  closely matching in compatibility with this emulator, scaled."
    )
    print(
        "- *LANG score*: The percentage of international languages tested\n"
        "  as having support, scaled."
    )
    print(
        "- *ZWJ score*: Determined by version release level of emoji sequences\n"
        "  with Zero-Width Joiner support, multiplied by the pct of emoji\n"
        "  sequences supported at that version, scaled."
    )
    print(
        "- *VS16 score*: Determined by the number of Emoji using Variation\n"
        "  Selector-16 supported as wide characters, scaled."
    )
    print()


def scale_scores(score_table, entry, key):
    my_score = entry[key]
    max_score = max([_entry[key] for _entry in score_table])
    min_score = min([_entry[key] for _entry in score_table])
    return (my_score - min_score) / (max_score - min_score)


def score_zwj(data):
    score = 0.0
    best_zwj_version = data["test_results"]["emoji_zwj_version"]
    if best_zwj_version:
        score = (
            list(data["test_results"]["emoji_zwj_results"].keys()).index(
                best_zwj_version
            )
            + 1
        ) / len(data["test_results"]["emoji_zwj_results"])
    score2 = 0.01
    if best_zwj_version:
        score2 = (
            data["test_results"]["emoji_zwj_results"][best_zwj_version]["pct_success"]
            / 100
        )
    return score * score2


def score_wide(data):
    score = 0.0
    best_wide_version = data["test_results"]["unicode_wide_version"]
    unicode_versions = list(data["test_results"]["unicode_wide_results"].keys())
    if best_wide_version and best_wide_version in unicode_versions:
        score = (unicode_versions.index(best_wide_version) + 1) / len(unicode_versions)
    score2 = 0.01
    if best_wide_version:
        score2 = (
            data["test_results"]["unicode_wide_results"][best_wide_version][
                "pct_success"
            ]
            / 100
        )
    return score * score2


def score_lang(data):
    _total_langs_supported = sum(
        1
        for lang in data["test_results"]["language_results"]
        if data["test_results"]["language_results"][lang]["n_errors"] == 0
    )
    _total_langs_available = len(data["test_results"]["language_results"])
    return _total_langs_supported / _total_langs_available


def do_details(score_table):
    h1_text = "Software details"
    print(h1_text)
    print("=" * len(h1_text))
    print()
    for entry in score_table:
        sw_name = entry["terminal_software_name"]
        print(".. _{}:".format(entry["terminal_software_name"].replace(" ", "_")))
        print()
        h2_text = sw_name
        print(h2_text)
        print("-" * len(h2_text))
        print()
        show_wide_character_support(sw_name, entry)


def show_wide_character_support(sw_name, entry):
    h3_text = "Wide character support"
    print(h3_text)
    print("+" * len(h3_text))
    print()
    print(
        f"The best wide unicode table version for {sw_name} appears to be \n"
        f'is {entry["version_best_wide"]}, this is from a summary of the following\n'
        f"results:"
    )
    print()
    print("")
    tabulated_wide_results = [
        {
            "version": version,
            "n_errors": result["n_errors"],
            "n_total": result["n_total"],
            "pct_success": result["pct_success"],
        }
        for version, result in entry["data"]["test_results"][
            "unicode_wide_results"
        ].items()
    ]
    print(tabulate.tabulate(tabulated_wide_results, headers="keys", tablefmt="rst"))
    print()

    unicode_versions = list(
        entry["data"]["test_results"]["unicode_wide_results"].keys()
    )
    version_best_wide = entry["version_best_wide"]
    show_failed_version = version_best_wide
    if (
        entry["data"]["test_results"]["unicode_wide_results"][show_failed_version][
            "n_errors"
        ]
        == 0
    ):
        # find another version with errors, to show
        for _, version in sorted(
            [
                (wcwidth._wcversion_value(v), v)
                for v in unicode_versions
                if wcwidth._wcversion_value(v)
                > wcwidth._wcversion_value(show_failed_version)
            ]
        ):
            if (
                entry["data"]["test_results"]["unicode_wide_results"][version][
                    "n_errors"
                ]
                > 0
            ):
                show_failed_version = version
                break
    if (
        entry["data"]["test_results"]["unicode_wide_results"][show_failed_version][
            "n_errors"
        ]
        > 0
    ):
        first_failure = entry["data"]["test_results"]["unicode_wide_results"][
            show_failed_version
        ]["failed_codepoints"][0]
        as_printf_hex = "".join(
            rf"\{hb[1:]}"
            for hb in map(hex, binascii.b2a_hex(first_failure["wchar"].encode("utf-8")))
        )
        print("Example shell test using printf(1) of a WIDE character ")
        print(f"from Unicode Version {show_failed_version}, python string ")
        print(f"``{repr(first_failure['wchar'])}`` as a utf-8 bytestring, ")
        print("``|`` should align in output::")
        print()
        print(rf'    $ printf "{as_printf_hex}|\\n12|')
        print(f'    {chr(int(first_failure["wchar"][2:], 16))}|')
        print(f"    12|")
        print()
        print(f"wcwidth measures width {first_failure['measured_by_wcwidth']},")
        print(f"while {sw_name} measures width {first_failure['measured_by_terminal']}")
        print()


if __name__ == "__main__":
    # python parse_results_to_rst.py > RESULTS.rst&& rst2html RESULTS.rst > results.html&& open results.html
    main()

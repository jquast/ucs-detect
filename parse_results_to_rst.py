#!/usr/bin/env python

import os
import yaml

import wcwidth

DATA_PATH = os.path.join(os.path.dirname(__file__), "data")

def main():
    graded_score_table = grade_with_scale(make_score_table())
    generate_reStructuredText_score_table(graded_score_table)

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
        score_wide_version = score_wide(data)

        # 'EMOJI ZWJ',
        version_best_zwj = data["test_results"]["emoji_zwj_version"]
        score_zwj_version = score_zwj(data)

        # 'EMOJI VS-16',
        score_emoji_vs16 = data["test_results"]["emoji_vs16_results"]["9.0.0"]["pct_success"] / 100

        # Language Support,
        score_language = score_lang(data)
        languages_successful = [lang for lang in data["test_results"]["language_results"]
                               if data["test_results"]["language_results"][lang]['n_errors'] == 0]
        languages_failed_by_pct = [
            (lang, data["test_results"]["language_results"][lang]["pct_success"])
            for lang in data["test_results"]["language_results"]
            if data["test_results"]["language_results"][lang]['n_errors'] > 0]

        score_table.append(dict(
            terminal_software_name=data['software'],
            terminal_software_version=data['version'],
            score_emoji_vs16=score_emoji_vs16,
            score_final=sum((score_language, score_emoji_vs16, score_zwj_version, score_wide_version)),
            score_language=score_language,
            score_wide_version=score_wide_version,
            score_zwj_version=score_zwj_version,
            version_best_wide=version_best_wide,
            version_best_zwj=version_best_zwj,
            languages_failed_by_pct=languages_failed_by_pct,
            languages_successful=languages_successful,
        ))
    return score_table

GRADES = ['F-', 'F', 'F+', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']

def make_grade(score):
    """
    Return grade string for score
    """
    return GRADES[int(score * (len(GRADES) - 1))]

def generate_reStructuredText_score_table(score_table):
    """
    Generate reStructuredText table from score_table
    """
    print(".. list-table:: Terminal Emulator Unicode Support")
    print("   :widths: 10 10 10 10 10 10 10 10 10 10 10")
    print("   :header-rows: 1")
    print("")
    print("   * - Terminal Software")
    print("     - SW Version")
    print("     - Score")
    print("     - Emoji VS-16")
    print("     - Emoji ZWJ")
    print("     - Emoji ZWJ Version")
    print("     - Unicode Wide")
    print("     - Unicode Wide Version")
    print("     - Language Support")
    print("     - Languages Successful")
    print("     - Languages Failed by Pct")
    for entry in score_table:
        print(entry)
        print(f"   * - {entry['terminal_software_name']}".format(**entry))
        print(f"     - {entry['terminal_software_version']}".format(**entry))
        print(f"     - {make_grade(entry['score_final_scaled'])}".format(**entry))
        print(f"     - {entry['score_emoji_vs16']:.2f}".format(**entry))
        print(f"     - {entry['score_zwj_version']:.2f}".format(**entry))
        print(f"     - {entry['version_best_zwj']}".format(**entry))
        print(f"     - {entry['score_wide_version']:.2f}".format(**entry))
        print(f"     - {entry['version_best_wide']}".format(**entry))
        print(f"     - {entry['score_language']:.2f}".format(**entry))
        print(f"     - {entry['languages_successful']}".format(**entry))
        print(f"     - {entry['languages_failed_by_pct']}".format(**entry))
        print("")
    print("")

def grade_with_scale(score_table):
    """
    Return modified score_table with additional attributes returned by '_scale'
    """
    result = []
    _score_keys = [key for key in score_table[0].keys() if key.startswith('score_')]
    for entry in score_table:
        for key in _score_keys:
            entry[key + '_scaled'] = scale_scores(score_table, entry, key)
        result.append(entry)
    return result

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
                list(data["test_results"]["emoji_zwj_results"].keys()).index(best_zwj_version) + 1
            ) / len(data["test_results"]["emoji_zwj_results"])
    return score

def score_wide(data):
    score = 0.0
    best_wide_version = data["test_results"]["unicode_wide_version"]
    unicode_versions = list(data["test_results"]["unicode_wide_results"].keys())
    if best_wide_version and best_wide_version in unicode_versions:
        score = (unicode_versions.index(best_wide_version) + 1) / len(unicode_versions)
    return score

def score_lang(data):
    _total_langs_supported = sum(1 for lang in data["test_results"]["language_results"]
                                    if data["test_results"]["language_results"][lang]['n_errors'] == 0)
    _total_langs_available = len(data["test_results"]["language_results"])
    return _total_langs_supported / _total_langs_available



if __name__ == "__main__":
    main()

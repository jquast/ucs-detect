#!/usr/bin/env python

import os
import yaml

# 3rd party
import wcwidth
import tabulate

DATA_PATH = os.path.join(os.path.dirname(__file__), "data")

def main():
    graded_score_table = grade_with_scale(make_score_table())
    generate_reStructuredText_score_table(summarize(graded_score_table))

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
            score_final=sum((score_language, score_emoji_vs16, score_zwj_version, score_wide_version)) / 4,
            score_language=score_language,
            score_wide_version=score_wide_version,
            score_zwj_version=score_zwj_version,
            version_best_wide=version_best_wide,
            version_best_zwj=version_best_zwj,
            languages_failed_by_pct=languages_failed_by_pct,
            languages_successful=languages_successful,
        ))
    return score_table

GRADES = ['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']

def make_grade(score):
    """
    Return grade string for score
    """
    return GRADES[int(score * (len(GRADES) - 1))]

def generate_reStructuredText_score_table(score_table):
    """
    Generate reStructuredText table from score_table
    """
    print(tabulate.tabulate(score_table, headers="keys", tablefmt="rst"))


def summarize(score_table):
    results = []
    for result in score_table:
        results.append({
            "Terminal Software": result["terminal_software_name"],
            "Software Version": result["terminal_software_version"],
            "FINAL score": make_grade(result["score_final_scaled"]) + f' ({result["score_final"]*100:.2f}%)',
            "WIDE score": make_grade(result["score_wide_version_scaled"]) + f' ({result["score_wide_version"]*100:.2f}%)',
            "Wide Unicode version": result["version_best_wide"] or '',
            "LANG score": make_grade(result["score_language_scaled"]) + f' ({result["score_language"]*100:.2f}%)',
            "ZWJ score": make_grade(result["score_zwj_version_scaled"]) + f' ({result["score_zwj_version"]*100:.2f}%)',
            "ZWJ Unicode version": result["version_best_zwj"] or '',
            "VS16 score": make_grade(result["score_emoji_vs16_scaled"]) + f' ({result["score_emoji_vs16"]*100:.2f}%)',
            })
    return results

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

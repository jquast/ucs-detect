"""Dump all XTGETTCAP capability names for each terminal in data/, by software name and version."""
from pathlib import Path

import yaml


def main():
    """Dump all XTGETTCAP terminfo capability names for each terminal."""
    data_dir = Path(__file__).resolve().parent / "data"
    yaml_files = sorted(data_dir.glob("*.yaml"))

    results = []
    for yf in yaml_files:
        with open(yf) as f:
            doc = yaml.safe_load(f)
        if doc is None:
            continue
        sw_name = doc.get("software_name", yf.stem)
        sw_ver = doc.get("software_version", "?")
        tr = doc.get("terminal_results", {})
        xtg = tr.get("xtgettcap", {})
        capabilities = xtg.get("capabilities", {}) if xtg.get("supported") else {}
        if capabilities:
            cap_names = sorted(capabilities.keys())
            results.append((sw_name, sw_ver, cap_names))

    for sw_name, sw_ver, caps in results:
        print(f'{sw_name} {sw_ver}: {", ".join(caps)}')


if __name__ == "__main__":
    main()

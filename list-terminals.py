#!/usr/bin/env python3
"""List all tested terminals sorted alphabetically."""
# this is really a sort of troubleshooting device, by reverse lookup
# of data gathered, sorted alphabetically, we can find duplicates from
# multiple versions or files or sometimes operating systems
import yaml


def list_terminals():
    """List all tested terminals sorted alphabetically."""
    from pathlib import Path
    data_dir = Path('data')
    terminals = []

    for yaml_file in sorted(data_dir.glob('*.yaml')):
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)

            system = data.get('system', 'Unknown')
            software_name = data.get('software_name', 'Unknown')
            software_version = data.get('software_version', 'Unknown')

            terminals.append({
                'name': software_name,
                'version': software_version,
                'file': yaml_file.name,
                'system': system
            })
        except Exception as e:
            print(f"Error reading {yaml_file}: {e}")

    # Print sorted alphabetically by name
    for term in sorted(terminals, key=lambda x: x['name'].lower()):
        print(f"python re-run.py data/{term['file']} #  {term['name']} {term['version']} ({term['system']})")

    # Print summary
    print(f"\nTotal: {len(terminals)} terminals")


if __name__ == '__main__':
    list_terminals()

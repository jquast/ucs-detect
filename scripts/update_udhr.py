#!/usr/bin/env python3
# Script to update UDHR text files from the unicode-org/udhr XML repository.
# Parses XML files from {tempdir}/udhr/data/udhr/ and generates plain text files
# in ucs_detect/udhr/ matching the existing format.

import xml.etree.ElementTree as ET
from pathlib import Path
import sys
import tempfile
import subprocess


def parse_udhr_xml(xml_path):
    # Parse UDHR XML file and extract content
    # Returns dict with: language_name, content (list of lines)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    ns = {'udhr': 'http://efele.net/udhr'}

    # Get language name
    lang_name = root.get('n', 'Unknown')

    content_lines = []

    # Get title
    title_elem = root.find('udhr:title', ns)
    if title_elem is not None and title_elem.text:
        content_lines.append(title_elem.text.strip())

    # Process notes (if any)
    notes_found = False
    for note in root.findall('udhr:note', ns):
        for para in note.findall('udhr:para', ns):
            if para.text:
                # No indentation - ucs-detect strips it anyway
                content_lines.append(para.text.strip())
                notes_found = True

    # Add blank line only if we had notes
    if notes_found:
        content_lines.append("")

    # Process preamble
    preamble = root.find('udhr:preamble', ns)
    if preamble is not None:
        preamble_title = preamble.find('udhr:title', ns)
        if preamble_title is not None and preamble_title.text:
            content_lines.append(preamble_title.text.strip())

        for para in preamble.findall('udhr:para', ns):
            if para.text:
                text = para.text.strip()
                content_lines.append(text)

        content_lines.append("")

    # Process articles
    for article in root.findall('udhr:article', ns):
        article_num = article.get('number', '')

        # Article title
        article_title = article.find('udhr:title', ns)
        if article_title is not None and article_title.text:
            content_lines.append(article_title.text.strip())

        # Check for ordered list (numbered sub-items)
        orderedlist = article.find('udhr:orderedlist', ns)
        if orderedlist is not None:
            content_lines.append("")
            for listitem in orderedlist.findall('udhr:listitem', ns):
                content_lines.append("")
                for para in listitem.findall('udhr:para', ns):
                    if para.text:
                        text = para.text.strip()
                        content_lines.append(text)
                content_lines.append("")
            content_lines.append("")
        else:
            # Regular paragraphs
            for para in article.findall('udhr:para', ns):
                if para.text:
                    text = para.text.strip()
                    content_lines.append(text)

        content_lines.append("")

    return {
        'language_name': lang_name,
        'content': content_lines
    }


def generate_text_file(xml_path, output_dir):
    # Generate a plain text file from a UDHR XML file
    # Returns path to generated file, or None if skipped
    xml_path = Path(xml_path)

    if xml_path.stem in ('index', 'template'):
        return None

    data = parse_udhr_xml(xml_path)
    output_file = output_dir / f"{xml_path.stem}.txt"

    header_lines = [
        f"Universal Declaration of Human Rights - {data['language_name']}",
        "",
        'This plain text version prepared by the "UDHR in XML" project,',
        "http://efele.net/udhr.",
        "",
        "-----",
        ""
    ]

    with open(output_file, 'w', encoding='utf-8') as f:
        for line in header_lines + data['content']:
            f.write(line + '\n')

    return output_file


def main():
    # Process all UDHR XML files
    xml_dir = Path(tempfile.gettempdir()) / 'udhr' / 'data' / 'udhr'
    output_dir = Path(__file__).parent / 'ucs_detect' / 'udhr'

    # yes, i know git submodules exist, no thank you ..
    if not xml_dir.exists():
        temp_dir = Path(tempfile.gettempdir())
        response = input("Clone UDHR repository to {temp_dir}? [y/n]: ").strip().lower()
        if response.startswith('y'):
            subprocess.check_call(
                ['git', 'clone', 'https://github.com/unicode-org/udhr.git'],
                cwd=temp_dir
            )

    # Get all XML files
    xml_files = sorted(xml_dir.glob('*.xml'))
    print(f"Found {len(xml_files)} XML files in {xml_dir}")

    # Process
    processed = 0
    skipped = 0
    errors = 0
    for xml_file in xml_files:
        result = generate_text_file(xml_file, output_dir)
        if result is None:
            skipped += 1
        elif result:
            processed += 1
        else:
            errors += 1

    print(f"Processed {processed} files, skipped {skipped}")
    if errors > 0:
        print(f"Errors: {errors} files", file=sys.stderr)

    # Apply encoding fixes for known issues in upstream XML
    print("\nApplying encoding fixes...")
    import fix_udhr_data
    fix_udhr_data.main()

    return errors


if __name__ == '__main__':
    sys.exit(main())

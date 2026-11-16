"""
Install and select GNU Unifont for terminal font tests.

Unifont 18.0.01 covers Unicode 18.0 in 116,638 glyphs between its two files.  Noto Sans Mono covers
about 3,300 glyphs and carries no emoji, so Unifont is the only one of the two that can render the
newest codepoints the tests draw.

Two files are required: ``unifont`` holds the basic multilingual plane, ``unifont_upper`` holds
planes 1 to 3, which include emoji.  Both are installed together and fontconfig is told to prefer
them for every monospace family and to fall back to them last for every other pattern.
"""

# std imports
import os
import sys
import time
import argparse
import subprocess
import urllib.request

FONT_VERSION = '18.0.01'

FONT_FILES = ('unifont', 'unifont_upper')

FONT_URL = ('https://unifoundry.com/pub/unifont/unifont-{version}'
            '/font-builds/{name}-{version}.otf')

FONT_FAMILIES = ('Unifont', 'Unifont Upper')

#: Families terminals name in their configuration, all redirected to Unifont.
FONT_ALIASES = (
    'monospace',
    'Monospace',
    'mono',
    'Menlo',
    'Consolas',
    'Cascadia Mono',
    'Cascadia Code',
    'DejaVu Sans Mono',
    'Liberation Mono',
    'FreeMono',
    'Noto Sans Mono',
    'JetBrains Mono',
    'Fira Code',
    'Ubuntu Mono',
    'Courier New',
)

MINIMUM_FONT_BYTES = 1000000


def font_paths(directory):
    """Return the two installed font paths below *directory*."""
    return [os.path.join(directory, f'{name}-{FONT_VERSION}.otf')
            for name in FONT_FILES]


def _download(url, path):
    last_error = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=120) as response:
                data = response.read()
            if len(data) < MINIMUM_FONT_BYTES:
                raise OSError(f'{url} returned {len(data)} bytes')
            if data[:4] not in (b'OTTO', b'\x00\x01\x00\x00'):
                raise OSError(f'{url} is not an OpenType font')
            temporary = f'{path}.tmp'
            with open(temporary, 'wb') as stream:
                stream.write(data)
            os.replace(temporary, path)
            return
        except OSError as error:
            last_error = error
            time.sleep(2 * (attempt + 1))
    raise OSError(f'unable to download {url}: {last_error}')


def install(directory, fontconfig_path=None, aliases=True):
    """Download both Unifont files into *directory* and update fontconfig."""
    os.makedirs(directory, exist_ok=True)
    paths = font_paths(directory)
    keep = {os.path.basename(path) for path in paths}
    for entry in os.listdir(directory):
        if (entry.endswith('.otf')
                and entry.startswith(('unifont-', 'unifont_upper-'))
                and entry not in keep):
            os.unlink(os.path.join(directory, entry))
    for name, path in zip(FONT_FILES, paths):
        if os.path.isfile(path) and os.path.getsize(path) >= MINIMUM_FONT_BYTES:
            continue
        _download(FONT_URL.format(version=FONT_VERSION, name=name), path)
    if fontconfig_path is not None:
        write_config(fontconfig_path, font_dir=directory, aliases=aliases)
    subprocess.run(['fc-cache', '-f', directory], check=False,
                   capture_output=True, timeout=120)


def fontconfig_xml(font_dir=None, include=None, aliases=True, cachedir=None,
                   font_dirs=()):
    """Return a fontconfig document preferring Unifont."""
    parts = ['<?xml version="1.0"?>',
             '<!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd">',
             '<fontconfig>']
    if cachedir:
        parts.append(f'  <cachedir>{cachedir}</cachedir>')
    if include:
        parts.append(f'  <include ignore_missing="yes">{include}</include>')
    for directory in ([font_dir] if font_dir else []) + list(font_dirs):
        parts.append(f'  <dir>{directory}</dir>')
    if aliases:
        for family in FONT_ALIASES:
            parts.append(f'  <alias binding="same"><family>{family}</family>')
            parts.append('    <prefer>')
            for preferred in FONT_FAMILIES:
                parts.append(f'      <family>{preferred}</family>')
            parts.append('    </prefer></alias>')
    parts.append('  <match target="pattern">')
    for fallback in FONT_FAMILIES:
        parts.append('    <edit name="family" mode="append_last" '
                     f'binding="weak"><string>{fallback}</string></edit>')
    parts.append('  </match>')
    parts.append('</fontconfig>')
    return '\n'.join(parts) + '\n'


def write_config(path, font_dir=None, include=None, aliases=True,
                 cachedir=None, font_dirs=()):
    """Write a fontconfig document to *path*."""
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as stream:
        stream.write(fontconfig_xml(
            font_dir, include, aliases, cachedir, font_dirs))


def ensure_system_fonts(project_dir):
    """Install Unifont below ``<project_dir>/fonts`` and return a fontconfig file."""
    project_dir = os.path.abspath(project_dir)
    directory = os.path.join(project_dir, 'fonts')
    install(directory)
    path = os.path.join(directory, 'system-fonts.conf')
    write_config(
        path, font_dir=directory, cachedir='~/.cache/fontconfig',
        font_dirs=('/usr/share/fonts', '/usr/local/share/fonts'))
    return path


def main(argv=None):
    """Entry point for the Docker build and for ad hoc system setup."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--install', action='store_true',
                        help='Download Unifont into --dest')
    parser.add_argument('--dest', default=None,
                        help='Font directory (default: beside this module)')
    parser.add_argument('--fontconfig', default=None,
                        help='Write a fontconfig file to this path')
    parser.add_argument('--print-config', action='store_true',
                        help='Print the fontconfig document and exit')
    parser.add_argument('--no-aliases', action='store_true',
                        help='Omit family aliases from the fontconfig document')
    args = parser.parse_args(argv)
    aliases = not args.no_aliases
    if args.print_config:
        sys.stdout.write(fontconfig_xml(dest_dir(args), None, aliases))
        return 0
    if args.install:
        directory = dest_dir(args)
        install(directory, args.fontconfig, aliases)
        return 0
    parser.print_help()
    return 2


def dest_dir(args):
    """Return the font directory for *args*."""
    if args.dest:
        return args.dest
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')


if __name__ == '__main__':
    sys.exit(main())

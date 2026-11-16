"""
Detect grapheme spillover by drawing contested text over truecolor cell blocks.

A page paints every terminal row with alternating truecolor cells.  The page is captured, the
graphemes are drawn over the same blocks, and the page is captured again.  Pixels that change
outside the cell range reported by the cursor are spillover.

The module also provides the candidate list, the scanner used by ``scripts/spillover_scan.py``, and
the atomic YAML writer used to record results in the terminal data file.
"""

# std imports
import os
import sys
import glob
import math
import time
import shutil
import tempfile
import functools
import subprocess
import collections
import unicodedata

# 3rd party
import yaml

# local
from ucs_detect import imaging, macos
from ucs_detect.tasks import TaskPool
from ucs_detect.measure import unicode_escape_string
from ucs_detect.accessories import display_lock, decode_wchars, load_document
from ucs_detect.table_ri_contested import RI_CONTESTED
from ucs_detect.table_zwj_contested import ZWJ_CONTESTED
from ucs_detect.table_lang_contested import LANG_CONTESTED
from ucs_detect.table_vs15_contested import VS15_CONTESTED
from ucs_detect.table_vs16_contested import VS16_CONTESTED

#: Cells painted to the left of the first tested cell.
LEFT_CELLS = 3

#: Emoji presentation kinds, in display order.  Their cell width is standardized, so a spill is
#: an error, and each kind receives its own evidence page.
EMOJI_KINDS = ('ZWJ', 'VS16', 'VS15', 'RI')

#: Most language evidence pages kept, one per distinct language.
MAX_LANGUAGE_EVIDENCE_IMAGES = 4

#: Most error page images kept per terminal: four emoji kinds plus four languages.
MAX_EVIDENCE_IMAGES = len(EMOJI_KINDS) + MAX_LANGUAGE_EVIDENCE_IMAGES

#: Short display names for spill categories that carry no language label.
SPILLOVER_KIND_NAMES = {
    'zwj': 'ZWJ',
    'vs16': 'VS16',
    'vs15': 'VS15',
    'ri': 'RI',
    'wide': 'WIDE',
    'narrow': 'NARROW',
}

#: Display order of non-language spill kinds.
KIND_ORDER = {kind: index for index, kind in enumerate(
    ('ZWJ', 'VS16', 'VS15', 'RI', 'WIDE', 'NARROW'))}

#: Cells between the start of one tested grapheme and the next, leaving 22 cells
#: for a 2-cell grapheme to spill right before the next tested cell.
COLUMN_STRIDE = 24

#: Zero based column where each tested grapheme begins.
START_COLUMN = LEFT_CELLS

#: Most tested columns placed on one page, so a window wider than the page layout is aimed at
#: does not paint a page wider than the capture path handles.
MAX_PAGE_COLUMNS = 10

#: Sum of channel differences treated as a different color.
COLOR_TOLERANCE = 60

#: Fraction of a cell that must differ before it is contaminated.
PAINTED_FRACTION = 0.02

#: Fraction of a row's cells that must disagree with the page before the row is called displaced.
SHIFT_FRACTION = 0.2

#: Frames per second of the spillover evidence animation.
ANIMATION_FPS = 6

#: Frames in one two second ramp up and ramp down loop.
ANIMATION_FRAMES = 12

#: Seconds between two captures that are compared to detect a frame still being painted.
SETTLE_DELAY = 0.2

#: Captures compared before a page is measured as it finally landed.
SETTLE_ATTEMPTS = 4

#: Bidirectional classes laid out right to left, including Arabic numbers, which a terminal that
#: applies the bidi algorithm places with the surrounding right to left text.
RTL_DIRECTIONS = ('R', 'AL', 'AN')

#: Palette slots the animation gives to the capture's own colors, exactly, most frequent first.
EXACT_PALETTE_COLORS = 128

#: gifsicle options that discard repeated frame data and merge near-duplicate colors, leaving the
#: frame size and the position of every pixel unchanged.
GIFSICLE_OPTIONS = ('-O3', '--lossy=80', '--colors', '128')

#: RGB and ANSI fallbacks for alternating row blocks.
BAR_COLORS = (
    ((64, 0, 192), '44', '21'),
    ((0, 160, 64), '42', '34'),
)

#: Glyph painted into every bar cell, so the cell is filled by a glyph and not only by a background
#: color.  A background alone leaves a previous page's glyphs outside their advance visible on
#: terminals that keep them.
BAR_GLYPH = '\u2588'

#: Rewrite every cell of a page, so a previous page's glyphs outside their advance are cleared.
#: The cursor is hidden here.
PAGE_CLEAR = '\x1b[0m\x1b[?25l\x1b[2J\x1b[H'

#: RGB and ANSI fallbacks for calibration row bands.
CALIBRATION_COLORS = (
    ((48, 0, 64), '44', '53'),
    ((0, 64, 48), '42', '23'),
)

#: RGB and ANSI fallbacks for the tested grapheme.
GLYPH_COLOR = ((255, 255, 255), '97', '231')

#: RGB and ANSI fallbacks for the tested grapheme background.
GLYPH_BACKGROUND = ((16, 16, 16), '40', '16')

RESET = '\x1b[0m'

#: Marker background sequences, most precise color last.
MARKER_MAGENTA = '\x1b[45m\x1b[105m\x1b[48;5;201m\x1b[48;2;255;0;255m'
MARKER_YELLOW = '\x1b[43m\x1b[103m\x1b[48;5;226m\x1b[48;2;255;255;0m'


class SpilloverError(RuntimeError):
    """Raised when calibration or capture cannot be completed."""


Candidate = collections.namedtuple(
    'Candidate', ('text', 'category', 'label', 'width', 'advance'),
    defaults=(None,))

#: Control glyphs that must fit in the advance reported by the terminal.
CONTROL_GRAPHEMES = (
    Candidate('A', 'control', 'ascii', 1),
    Candidate('中', 'control', 'cjk', 2),
)


Calibration = collections.namedtuple(
    'Calibration', ('origin_x', 'origin_y', 'cell_width', 'cell_height',
                    'term_width', 'term_height'))


Spillover = collections.namedtuple(
    'Spillover', ('index', 'page', 'row', 'column', 'candidate',
                  'left_cells', 'right_cells', 'blank', 'evidence'),
    defaults=(None,))


def spillover_rate(n_spillover, n_tested):
    """Return the fraction of tested contested graphemes with spillover."""
    if not n_tested:
        return float('nan')
    return n_spillover / n_tested


def emoji_spill_counts(section):
    """
    Return ``(n_spillover, n_tested)`` for the emoji kinds of *section*.

    Only ZWJ, VS16, VS15, and RI sequences have a standardized width, so only their spills are an
    error; language graphemes are reported and left unscored.
    """
    tested = section.get('n_tested_by_kind') or {}
    spilled = section.get('spill_counts_by_kind') or {}
    if not any(tested.get(kind) for kind in EMOJI_KINDS):
        return None
    n_tested = sum(tested.get(kind) or 0 for kind in EMOJI_KINDS)
    n_spillover = sum((spilled.get(kind) or {}).get('graphemes_any') or 0
                      for kind in EMOJI_KINDS)
    return n_spillover, n_tested


def emoji_spillover_rate(section):
    """Return the spill rate of the emoji kinds, or ``nan`` when there are no counts."""
    counts = emoji_spill_counts(section)
    if counts is None:
        return float('nan')
    return spillover_rate(*counts)


def scaled_spillover_score(rate, min_rate, max_rate):
    """
    Return an inverted 0 to 1 score for a spill rate.

    The lowest observed rate scores 1.0 and the highest scores 0.0.
    """
    if math.isnan(rate):
        return float('nan')
    if max_rate == min_rate:
        return 1.0
    return 1.0 - ((rate - min_rate) / (max_rate - min_rate))


def spillover_statistics_from_amounts(amounts):
    """Return direction and amount counts from ``(left, right)`` cell pairs."""
    left = collections.Counter()
    right = collections.Counter()
    n_left = n_right = n_both = 0
    for left_cells, right_cells in amounts:
        left_cells = int(left_cells or 0)
        right_cells = int(right_cells or 0)
        if left_cells > 0:
            n_left += 1
            left[left_cells] += 1
        if right_cells > 0:
            n_right += 1
            right[right_cells] += 1
        if left_cells > 0 and right_cells > 0:
            n_both += 1
    return {
        'graphemes_any': n_left + n_right - n_both,
        'graphemes_left': n_left,
        'graphemes_right': n_right,
        'graphemes_both': n_both,
        'left_cells': {str(amount): count
                       for amount, count in sorted(left.items())},
        'right_cells': {str(amount): count
                        for amount, count in sorted(right.items())},
        'max_left_cells': max(left, default=0),
        'max_right_cells': max(right, default=0),
    }


def spillover_statistics(results):
    """Return :func:`spillover_statistics_from_amounts` for scan *results*."""
    return spillover_statistics_from_amounts(
        (result.left_cells, result.right_cells) for result in results)


def spillover_statistics_from_records(records):
    """Return :func:`spillover_statistics_from_amounts` for YAML *records*."""
    return spillover_statistics_from_amounts(
        ((record.get('spill_left_cells') or 0,
          record.get('spill_right_cells') or 0)
         for record in records))


def evidence_filename(number, codepoint, prefix=None):
    """
    Return the page evidence filename for page *number* and *codepoint*.

    *prefix* names the terminal: Sphinx copies images into one ``_images`` directory by basename,
    where two terminals spilling the same grapheme on the same page would overwrite each other.
    """
    name = f'spillover_{number:03d}_U+{codepoint:04X}.gif'
    return f'{prefix}-{name}' if prefix else name


def spillover_kind(category, label=None):
    """Return the short kind name of a spill category."""
    if category == 'language':
        return label or 'LANG'
    return SPILLOVER_KIND_NAMES.get(category, (category or 'Unknown').upper())


def explicit_unicode_escape(codepoints):
    r"""
    Return an always-explicit Python escape sequence for *codepoints*.

    Every codepoint uses ``\u`` or ``\U`` so the table shows hex rather than a character a font can
    render as a different glyph.
    """
    return "'" + ''.join(
        f'\\u{codepoint:04x}' if codepoint <= 0xffff
        else f'\\U{codepoint:08x}'
        for codepoint in codepoints) + "'"


def spillover_examples(results):
    """Return one representative example per kind, direction, and cell length."""
    examples = {}
    for result in results:
        left_cells = result.left_cells or 0
        right_cells = result.right_cells or 0
        if not left_cells and not right_cells:
            continue
        candidate = result.candidate
        kind = spillover_kind(candidate.category, candidate.label)
        width = max(1, min(candidate.advance or candidate.width,
                           COLUMN_STRIDE))
        example = explicit_unicode_escape(
            ord(char) for char in candidate.text)
        for direction, cells in (('Left', left_cells),
                                 ('Right', right_cells)):
            if cells:
                examples.setdefault(kind, {}).setdefault(
                    direction, {}).setdefault(
                        str(cells), {'example': example, 'width': width})
    return examples


def record_kind(record):
    """Return the kind of a YAML spill record."""
    return spillover_kind(record.get('category'), record.get('label'))


def evidence_kind_counts(record):
    """Return ``{kind: spill_count}`` for one evidence page record."""
    return collections.Counter(
        record_kind(spill) for spill in record.get('spillovers') or [])


def spillover_examples_from_records(records):
    """Return :func:`spillover_examples` for YAML spill *records*."""
    examples = {}
    for record in records:
        left_cells = record.get('spill_left_cells') or 0
        right_cells = record.get('spill_right_cells') or 0
        if not left_cells and not right_cells:
            continue
        codepoints = record.get('codepoints')
        if not codepoints:
            codepoints = [ord(char) for char in
                          decode_wchars(record.get('wchar') or '')]
        example = {
            'example': explicit_unicode_escape(codepoints),
            'width': record.get('advance') or 1,
        }
        kind = record_kind(record)
        for direction, cells in (('Left', left_cells),
                                 ('Right', right_cells)):
            if cells:
                examples.setdefault(kind, {}).setdefault(
                    direction, {}).setdefault(str(cells), example)
    return examples


def ranked_evidence_pages(image_records, limit=MAX_EVIDENCE_IMAGES):
    """Return evidence page filenames in display order."""
    pages = []
    for filename, record in image_records.items():
        spills = record.get('spillovers') or []
        if not spills:
            continue
        pages.append({
            'filename': filename,
            'counts': evidence_kind_counts(record),
            'languages': collections.Counter(
                spillover_kind('language', spill.get('label'))
                for spill in spills
                if spill.get('category') == 'language'),
            'total': len(spills),
            'page': record.get('page', 0),
        })

    selected = []
    selected_names = set()

    def add(page):
        if page['filename'] in selected_names:
            return False
        selected.append(page['filename'])
        selected_names.add(page['filename'])
        return True

    for kind in EMOJI_KINDS:
        candidates = [page for page in pages if page['counts'].get(kind)]
        if candidates:
            add(max(candidates, key=lambda page, kind=kind: (
                page['counts'][kind], page['total'], page['page'],
                page['filename'])))

    languages = {}
    for page in pages:
        for kind, count in page['languages'].items():
            score = (count, page['total'], page['page'], page['filename'])
            if kind not in languages or score > languages[kind][0]:
                languages[kind] = (score, page)
    ranked = sorted(
        languages.items(), key=lambda item: item[1][0], reverse=True)
    added_languages = 0
    for _kind, (_score, page) in ranked:
        if added_languages >= MAX_LANGUAGE_EVIDENCE_IMAGES:
            break
        if add(page):
            added_languages += 1
    return selected[:limit]


def prune_evidence(evidence_pages, evidence_dir, results, image_records,
                   limit=MAX_EVIDENCE_IMAGES):
    """Delete evidence files outside the kept set and clear their references."""
    keep_names = set(ranked_evidence_pages(image_records, limit))
    for entry in evidence_pages:
        filename = entry[1]
        if filename not in keep_names:
            try:
                os.unlink(os.path.join(evidence_dir, filename))
            except OSError:
                pass
    results = [
        result._replace(evidence=None)
        if result.evidence not in keep_names else result
        for result in results]
    image_records = {
        filename: record for filename, record in image_records.items()
        if filename in keep_names}
    return results, image_records


def remove_stale_evidence(evidence_dir, keep_names, prefix=None):
    """
    Delete evidence images in *evidence_dir* that *keep_names* does not name.

    A filename carries the page number and first codepoint of its run, so a later run writes new
    names and leaves the earlier pages behind.
    """
    patterns = ['spillover_*.gif']
    if prefix:
        patterns.append(f'{prefix}-spillover_*.gif')
    stale = set()
    for pattern in patterns:
        stale.update(glob.glob(os.path.join(evidence_dir, pattern)))
    for path in stale:
        if os.path.basename(path) in keep_names:
            continue
        try:
            os.unlink(path)
        except OSError:
            pass


def column_count(term_width):
    """Return how many tested columns fit across *term_width* cells."""
    return max(1, min(MAX_PAGE_COLUMNS,
                      (term_width - START_COLUMN) // COLUMN_STRIDE))


def cursor_guard(term_height, count):
    """
    Return the first row and row count hidden behind the terminal's own pointer, or None.

    A terminal that draws client side cursors has its pointer composited into the window at the rest
    position, the centre of the window, where hiding the X pointer cannot reach it.
    """
    count = min(count, max(0, term_height - 2))
    if count <= 0:
        return None
    return max(1, term_height // 2 - count // 2), count


def guard_row(row, guard):
    """Return the terminal row of published row *row*, stepping over the guard rows."""
    if guard and row >= guard[0]:
        return row + guard[1]
    return row


def page_layout(term_width, term_height, guard=None):
    """Return content rows and columns per page, leaving the pointer rows empty."""
    hidden = guard[1] if guard else 0
    return max(1, term_height - 1 - hidden), column_count(term_width)


def _sgr_background(rgb, ansi, cube, truecolor=False):
    if truecolor:
        return f'\x1b[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m'
    return (f'\x1b[{ansi}m\x1b[48;5;{cube}m'
            f'\x1b[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m')


def _sgr_foreground(rgb, ansi, cube, truecolor=False):
    if truecolor:
        return f'\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m'
    return (f'\x1b[{ansi}m\x1b[38;5;{cube}m'
            f'\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m')


def supports_truecolor(term):
    """Return True when the terminal reports more than 256 colors."""
    return getattr(term, 'number_of_colors', 0) >= 1 << 24


def _marker_cells(truecolor=False):
    del truecolor
    row1 = MARKER_MAGENTA + ' ' + MARKER_YELLOW + ' ' + RESET
    row2 = MARKER_YELLOW + ' ' + MARKER_MAGENTA + ' ' + RESET
    return row1, row2


def has_rtl_text(text):
    """Return True when *text* contains a character laid out right to left."""
    return any(unicodedata.bidirectional(char) in RTL_DIRECTIONS
               for char in text)


def without_rtl(candidates):
    """Return the candidates that contain no right to left characters."""
    return [candidate for candidate in candidates
            if not has_rtl_text(candidate.text)]


def contested_graphemes():
    """Return every multiple codepoint grapheme in the contested tables."""
    seen = set()
    result = []

    def add(text, category, label, width):
        if len(text) < 2 or text in seen or width < 1:
            return
        seen.add(text)
        result.append(Candidate(text, category, label, width))

    for width, languages in LANG_CONTESTED:
        for label, graphemes in languages:
            for text in graphemes:
                add(text, 'language', label, width)

    for category, table, width in (
            ('zwj', ZWJ_CONTESTED, 2),
            ('ri', RI_CONTESTED, 2),
            ('vs15', VS15_CONTESTED, 1),
            ('vs16', VS16_CONTESTED, 2)):
        for _version, sequences in table:
            for sequence in sequences:
                add(''.join(chr(codepoint) for codepoint in sequence),
                    category, '', width)

    return result


def measured_advances(document):
    """Return grapheme to terminal measured advance from a terminal YAML."""
    measured = {}
    test_results = document.get('test_results') or {}
    for key, value in test_results.items():
        if key == 'language_results':
            for language in value.values():
                for record in language.get('failed') or []:
                    text = decode_wchars(
                        record.get('wchars') or record.get('wchar') or '')
                    advance = record.get('measured_by_terminal')
                    if text and isinstance(advance, int) and advance > 0:
                        measured[text] = advance
            continue
        if not isinstance(value, dict):
            continue
        for version in value.values():
            for record in version.get('failed_codepoints') or []:
                text = decode_wchars(
                    record.get('wchars') or record.get('wchar') or '')
                advance = record.get('measured_by_terminal')
                if text and isinstance(advance, int) and advance > 0:
                    measured[text] = advance
    return measured


def apply_measured_advances(candidates, document):
    """Return *candidates* with terminal measured advances applied."""
    measured = measured_advances(document)
    result = []
    for candidate in candidates:
        if candidate.text in measured:
            result.append(candidate._replace(
                advance=measured[candidate.text]))
        else:
            result.append(candidate._replace(advance=candidate.width))
    return result


def candidate_rows(candidates):
    """Return YAML friendly rows describing *candidates*."""
    rows = []
    for index, candidate in enumerate(candidates):
        rows.append({
            'index': index,
            'wchar': unicode_escape_string(candidate.text),
            'codepoints': [ord(char) for char in candidate.text],
            'category': candidate.category,
            'label': candidate.label,
            'width': candidate.width,
        })
    return rows


def render_blank_page(rows, term_width, origin_row=0, truecolor=False):
    """Return escape text painting *rows* full width blocks."""
    parts = []
    last_column = max(1, term_width - 1)
    for row in range(origin_row, origin_row + rows):
        parts.append(f'\x1b[{row + 1};1H')
        for column in range(last_column):
            rgb, ansi, cube = BAR_COLORS[column % 2]
            parts.append(_sgr_background(rgb, ansi, cube, truecolor))
            parts.append(_sgr_foreground(rgb, ansi, cube, truecolor))
            parts.append(BAR_GLYPH)
        parts.append(RESET)
    parts.append(f'\x1b[{origin_row + 1};1H')
    return ''.join(parts)


def render_grapheme_at(row, column, text, truecolor=False):
    """Return escape text drawing *text* at a terminal cell."""
    return ''.join((
        f'\x1b[{row + 1};{column + 1}H',
        _sgr_background(*GLYPH_BACKGROUND, truecolor),
        _sgr_foreground(*GLYPH_COLOR, truecolor),
        text,
        RESET,
    ))


def render_page(origin_row, rows, term_width, items, truecolor=False):
    """Return a page with blocks painted and *items* drawn over them."""
    page = ''.join(
        [render_blank_page(rows, term_width, origin_row, truecolor)]
        + [render_grapheme_at(origin_row + row, column, text, truecolor)
           for row, column, text in items])
    # paint twice (workaround tecolot bug)
    return PAGE_CLEAR + page + page


def render_calibration(term_width, term_height, truecolor=False):
    """Return escape text for a calibration page."""
    parts = [PAGE_CLEAR]
    rows = max(1, term_height - 1)
    for row in range(rows):
        parts.append(f'\x1b[{row + 1};1H')
        parts.append(_sgr_background(*CALIBRATION_COLORS[row % 2], truecolor))
        parts.append(' ' * max(1, term_width - 1))
        parts.append(RESET)

    row1, row2 = _marker_cells(truecolor)
    parts.append(f'\x1b[1;1H{row1}')
    parts.append(f'\x1b[2;1H{row2}')

    bottom_row = max(3, term_height - 2)
    bottom_col = max(3, term_width - 2)
    parts.append(f'\x1b[{bottom_row};{bottom_col}H{row1}')
    parts.append(f'\x1b[{bottom_row + 1};{bottom_col}H{row2}')
    return ''.join(parts)


def _checkerboard_blocks(image):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return imaging.capture_marker_blocks(image)


def _marker_shaped(block, size):
    width = block[2] - block[0] + 1
    height = block[3] - block[1] + 1
    if width > size[0] / 4 or height > size[1] / 4:
        return False
    return 0.2 <= width / height <= 5.0


def _color_bounds(image):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    width, height = image.size
    px = image.load()
    x1 = y1 = width
    x2 = y2 = 0
    found = False
    for y in range(height):
        for x in range(width):
            red, green, blue = px[x, y]
            if max(red, green, blue) - min(red, green, blue) > 40:
                found = True
                x1 = min(x1, x)
                x2 = max(x2, x)
                y1 = min(y1, y)
                y2 = max(y2, y)
    if not found:
        return None
    return x1, y1, x2, y2


def calibration_from_image(image, term_width, term_height):
    """Return calibration metrics measured from a calibration capture."""
    blocks = [block for block in _checkerboard_blocks(image)
              if _marker_shaped(block, image.size)]
    if len(blocks) >= 2:
        top = min(blocks, key=lambda block: block[1])
        bottom = max(blocks, key=lambda block: block[1])
        origin_x, origin_y = top[0], top[1]
        column_span = max(1, term_width - 3)
        row_span = max(1, term_height - 3)
        cell_width = (bottom[0] - top[0]) / column_span
        cell_height = (bottom[1] - top[1]) / row_span
    elif len(blocks) == 1:
        # Wayland clients nested in a smaller compositor window can clip one marker, and a title
        # bar drawn inside the window can eat the top one.  The remaining marker is two cells wide
        # and two cells high and sits at a corner of the grid, so where it is says which one it is:
        # the far corner has to be walked back over the page to reach the origin.
        block = blocks[0]
        cell_width = (block[2] - block[0] + 1) / 2.0
        cell_height = (block[3] - block[1] + 1) / 2.0
        far = (block[1] + block[3]) / 2 > image.size[1] / 2
        origin_x = block[0]
        origin_y = block[1]
        if far:
            origin_x -= max(1, term_width - 3) * cell_width
            origin_y -= max(1, term_height - 3) * cell_height
    else:
        bounds = _color_bounds(image)
        if bounds is None:
            raise SpilloverError('calibration markers and color bands not found')
        origin_x, origin_y, right, bottom = bounds
        cell_width = (right - origin_x + 1) / max(1, term_width)
        cell_height = (bottom - origin_y + 1) / max(1, term_height)

    if not 2.0 <= cell_width <= 64.0:
        raise SpilloverError(f'implausible cell width {cell_width:.2f}')
    if not 2.0 <= cell_height <= 64.0:
        raise SpilloverError(f'implausible cell height {cell_height:.2f}')

    return Calibration(origin_x, origin_y, cell_width, cell_height,
                       term_width, term_height)


def analyze_calibration(path, term_width, term_height):
    """Return calibration metrics measured from image at *path*."""
    # 3rd party
    from PIL import Image
    with Image.open(path) as image:
        return calibration_from_image(image.copy(), term_width, term_height)


def refine_cell_width(path, calibration, row=None, max_relative_error=0.05):
    """
    Return *calibration* with its cell width and origin fitted to a bar row in *path*.

    Corner markers give a width good to a few percent, which is half a cell two hundred columns
    away, where every cell straddles two bars and reads as contaminated.
    """
    # 3rd party
    from PIL import Image

    with Image.open(path) as image:
        return refine_cell_width_from_image(
            image.convert('RGB'), calibration, row, max_relative_error)


def refine_cell_width_from_image(image, calibration, row=None,
                                 max_relative_error=0.05):
    """Return :func:`refine_cell_width` for an already opened *image*."""
    pixels = image.load()
    if row is None:
        row = calibration.term_height - 1
    y = int(round(calibration.origin_y
                  + (row + 0.5) * calibration.cell_height))
    y = max(0, min(y, image.height - 1))
    colors = [pixels[x, y][:3] for x in range(image.width)]
    transitions = [x for x in range(1, len(colors))
                   if colors[x] != colors[x - 1]]
    lowest = 0.7 * calibration.cell_width
    highest = 1.3 * calibration.cell_width
    candidates = [(earlier, later) for earlier, later
                  in zip(transitions, transitions[1:])
                  if lowest <= later - earlier <= highest]
    if len(candidates) < 10:
        return calibration
    gaps = sorted(later - earlier for earlier, later in candidates)
    rough = gaps[len(gaps) // 2]
    whole = [(earlier, later) for earlier, later in candidates
             if abs(later - earlier - rough) <= 1.5]
    if len(whole) < 10:
        return calibration
    pitch = sum(later - earlier for earlier, later in whole) / len(whole)
    if not 2.0 <= pitch <= 64.0:
        return calibration
    if abs(pitch - calibration.cell_width) > (
            max_relative_error * calibration.cell_width):
        return calibration
    residuals = sorted(
        earlier - round((earlier - calibration.origin_x) / pitch) * pitch
        for earlier, _later in whole)
    return calibration._replace(
        origin_x=residuals[len(residuals) // 2], cell_width=pitch)


def _cell_box(calibration, row, column, size=None):
    x0 = int(round(calibration.origin_x
                   + column * calibration.cell_width))
    x1 = int(round(calibration.origin_x
                   + (column + 1) * calibration.cell_width))
    y0 = int(round(calibration.origin_y
                   + row * calibration.cell_height))
    y1 = int(round(calibration.origin_y
                   + (row + 1) * calibration.cell_height))
    if size is not None:
        width, height = size
        x0 = max(0, min(x0, width - 1))
        y0 = max(0, min(y0, height - 1))
        x1 = max(x0 + 1, min(x1, width))
        y1 = max(y0 + 1, min(y1, height))
    return x0, y0, max(x0 + 1, x1), max(y0 + 1, y1)


def _inner_box(box, fraction=0.2):
    x0, y0, x1, y1 = box
    margin_x = max(1, int((x1 - x0) * fraction))
    margin_y = max(1, int((y1 - y0) * fraction))
    inner_x0 = min(x0 + margin_x, x1 - 1)
    inner_y0 = min(y0 + margin_y, y1 - 1)
    return (inner_x0, inner_y0,
            max(inner_x0 + 1, x1 - margin_x),
            max(inner_y0 + 1, y1 - margin_y))


def _color_distance(first, second):
    return (abs(first[0] - second[0])
            + abs(first[1] - second[1])
            + abs(first[2] - second[2]))


def reference_colors(image, calibration, row=None):
    """Return one reference RGB per terminal column."""
    if image.width < 1 or image.height < 1:
        raise SpilloverError('empty page capture')
    pixels = image.load()
    if row is None:
        row = calibration.term_height - 1
    colors = []
    for column in range(calibration.term_width):
        x0, y0, x1, y1 = _inner_box(
            _cell_box(calibration, row, column, image.size))
        samples = []
        for y in range(y0, y1):
            for x in range(x0, x1):
                samples.append(pixels[x, y][:3])
        if not samples:
            colors.append((0, 0, 0))
            continue
        samples.sort()
        colors.append(samples[len(samples) // 2])
    return colors


def cell_contamination(image, calibration, row, column, expected):
    """Return the fraction of a cell that differs from *expected*."""
    pixels = image.load()
    x0, y0, x1, y1 = _inner_box(
        _cell_box(calibration, row, column, image.size))
    total = 0
    different = 0
    step = max(1, int(calibration.cell_width // 5))
    for y in range(y0, y1, step):
        for x in range(x0, x1, step):
            total += 1
            if _color_distance(pixels[x, y][:3], expected) > COLOR_TOLERANCE:
                different += 1
    return different / total if total else 0.0


def _last_usable_column(image, calibration, reference_row, reference):
    last = max(0, calibration.term_width - 2)
    if reference_row is None:
        return last
    for column in range(last, -1, -1):
        if (cell_contamination(image, calibration, reference_row, column,
                               reference[column]) <= PAINTED_FRACTION):
            return column
    return 0


def cell_is_painted(image, calibration, row, column):
    """Return True when a cell contains pixels unlike its dominant color."""
    pixels = image.load()
    x0, y0, x1, y1 = _inner_box(
        _cell_box(calibration, row, column, image.size))
    samples = []
    for y in range(y0, y1):
        for x in range(x0, x1):
            samples.append(pixels[x, y][:3])
    if not samples:
        return False
    counts = collections.Counter(samples)
    dominant = counts.most_common(1)[0][0]
    different = sum(1 for sample in samples
                    if _color_distance(sample, dominant) > COLOR_TOLERANCE)
    return different / len(samples) > PAINTED_FRACTION


def _cell_colors(image, calibration, rows):
    pixels = image.load()
    colors = {}
    for row in rows:
        row_colors = []
        for column in range(calibration.term_width):
            x0, y0, x1, y1 = _inner_box(
                _cell_box(calibration, row, column, image.size))
            step_x = max(1, (x1 - x0) // 2)
            step_y = max(1, (y1 - y0) // 2)
            samples = [pixels[x, y][:3]
                       for y in range(y0 + step_y // 2, y1, step_y)
                       for x in range(x0 + step_x // 2, x1, step_x)]
            counts = collections.Counter(samples)
            row_colors.append(
                counts.most_common(1)[0][0] if counts else (0, 0, 0))
        colors[row] = row_colors
    return colors


def shifted_rows(image, calibration, rows):
    """Return the rows whose bars do not line up with the rest of the page."""
    rows = list(dict.fromkeys(rows))
    if len(rows) < 2:
        return []
    sampled = _cell_colors(image, calibration, rows)
    color_counts = collections.Counter(
        color for row in rows for color in sampled[row])
    bar_colors = [color for color, _count in color_counts.most_common(2)]
    if len(bar_colors) < 2:
        return []

    def is_page_bar(color):
        return min(_color_distance(color, bar_color)
                   for bar_color in bar_colors) <= COLOR_TOLERANCE

    agreed = []
    for column in range(calibration.term_width):
        counts = collections.Counter(
            sampled[row][column] for row in rows
            if is_page_bar(sampled[row][column]))
        agreed.append(counts.most_common(1)[0][0] if counts else None)
    shifted = []
    for row in rows:
        different = compared = 0
        for column, expected in enumerate(agreed):
            if expected is None:
                continue
            color = sampled[row][column]
            if not is_page_bar(color):
                continue
            compared += 1
            if _color_distance(color, expected) > COLOR_TOLERANCE:
                different += 1
        if compared and different / compared > SHIFT_FRACTION:
            shifted.append(row)
    return shifted


def row_has_bars(image, calibration, row):
    """Return True when *row* shows two alternating bar colors."""
    sampled = _cell_colors(image, calibration, [row])[row]
    counts = collections.Counter(sampled)
    if len(counts) < 2:
        return False
    (first, first_count), (second, second_count) = counts.most_common(2)
    share = (first_count + second_count) / calibration.term_width
    return share >= 0.8 and _color_distance(first, second) > COLOR_TOLERANCE


def visible_rows(image, calibration):
    """
    Return how many rows of *image* carry bars, counting from the top.

    An OpenGL terminal settles its viewport at the size it was launched with, so rows below a resize
    stay unpainted while the pty reports the larger size.
    """
    rows = 0
    for row in range(calibration.term_height):
        bottom = int(round(calibration.origin_y
                           + (row + 1) * calibration.cell_height))
        if bottom > image.height:
            break
        if not row_has_bars(image, calibration, row):
            break
        rows += 1
    return rows


def page_has_bars(image, calibration, row=None):
    """
    Return True when *row* shows two alternating bar colors.

    A frame that never reached the framebuffer is one flat color, and measuring against it reports
    spillover in every cell.
    """
    if row is None:
        row = calibration.term_height - 1
    return row_has_bars(image, calibration, row)


def analyze_page(image, calibration, items, reference=None,
                 reference_row=None):
    """Classify a single page capture, returning one result per item."""
    if reference is None:
        reference = reference_colors(image, calibration)
    columns_by_row = collections.defaultdict(set)
    for row, column, _candidate in items:
        columns_by_row[row].add(column)
    last_usable = _last_usable_column(
        image, calibration, reference_row, reference)

    results = []
    previous_by_row = {}
    for row, column, candidate in items:
        advance = candidate.advance or candidate.width
        advance = max(1, min(advance, COLUMN_STRIDE))
        blank = not any(
            cell_is_painted(image, calibration, row, cell)
            for cell in range(column, column + advance))

        left_start = max(0, column - LEFT_CELLS)
        previous = previous_by_row.get(row)
        if previous is not None:
            previous_column, previous_advance, previous_right = previous
            previous_end = (previous_column + previous_advance
                            + previous_right)
            left_start = max(left_start, previous_end)
        left_cells = 0
        for cell in range(column - 1, left_start - 1, -1):
            expected = reference[cell]
            if (cell_contamination(image, calibration, row, cell,
                                   expected) > PAINTED_FRACTION):
                left_cells = column - cell
            else:
                break

        first_gap = column + advance
        next_column = column + COLUMN_STRIDE
        if next_column in columns_by_row[row]:
            contiguous_end = min(next_column - 1,
                                 calibration.term_width - 2)
            isolated_end = min(contiguous_end,
                               next_column - LEFT_CELLS - 1)
        else:
            contiguous_end = isolated_end = last_usable
        scan_end = max(contiguous_end, isolated_end)
        dirty = [
            cell_contamination(image, calibration, row, cell,
                               reference[cell]) > PAINTED_FRACTION
            for cell in range(first_gap, scan_end + 1)
        ]
        right_cells = 0
        for offset in range(contiguous_end - first_gap + 1):
            if not dirty[offset]:
                break
            right_cells = offset + 1
        for offset in range(isolated_end - first_gap + 1):
            if dirty[offset]:
                right_cells = max(right_cells, offset + 1)

        previous_by_row[row] = (column, advance, right_cells)
        results.append({
            'left_cells': left_cells,
            'right_cells': right_cells,
            'blank': blank,
        })
    return results


def spilled_boxes(calibration, spills, size):
    """Return the pixel boxes of every contaminated cell."""
    boxes = []
    for row, column, candidate, left_cells, right_cells in spills:
        advance = max(1, min(candidate.advance or candidate.width,
                             COLUMN_STRIDE))
        cells = list(range(max(0, column - left_cells), column))
        cells += list(range(
            column + advance,
            min(column + advance + right_cells, calibration.term_width)))
        boxes.extend(
            _cell_box(calibration, row, cell, size) for cell in cells)
    return boxes


def _animation_palette(image, half):
    """
    Return a palette image holding the animation colors.

    A GIF carries one color table for the whole animation, so every frame maps through the same
    palette.
    """
    # 3rd party
    from PIL import Image

    sampled = image.getcolors(1 << 18)
    if sampled is None:
        return image.quantize(colors=256)
    sampled.sort(key=lambda item: -item[0])
    ordered = [color for _count, color in sampled[:EXACT_PALETTE_COLORS]]
    seen = set(ordered)
    for _count, color in sampled:
        if len(ordered) >= 256:
            break
        inverse = tuple(255 - channel for channel in color)
        for index in range(ANIMATION_FRAMES):
            amount = abs(index - half) / half
            blend = tuple(
                int(round(channel + (wanted - channel) * amount))
                for channel, wanted in zip(color, inverse))
            if blend not in seen:
                seen.add(blend)
                ordered.append(blend)
                if len(ordered) >= 256:
                    break
    flat = [0, 0, 0] * 256
    for index, color in enumerate(ordered):
        flat[index * 3:index * 3 + 3] = color
    palette = Image.new('P', (256, 1))
    palette.putpalette(flat)
    return palette


@functools.lru_cache(maxsize=None)
def _gifsicle_path():
    """Return the gifsicle executable, warning once per process when it is missing."""
    executable = shutil.which('gifsicle')
    if executable is None:
        print('warning: gifsicle not found, animations are left unoptimized',
              file=sys.stderr)
    return executable


def optimize_gif(path):
    """Shrink the GIF at *path* with gifsicle, keeping it unchanged when that fails."""
    executable = _gifsicle_path()
    if executable is None:
        return
    temporary = f'{path}.gifsicle'
    try:
        subprocess.run([executable, *GIFSICLE_OPTIONS, path, '-o', temporary],
                       check=True, capture_output=True)
        os.replace(temporary, path)
    except (OSError, subprocess.CalledProcessError) as error:
        print(f'warning: gifsicle failed for {path}: {error}', file=sys.stderr)
        try:
            os.unlink(temporary)
        except OSError:
            pass


def write_spillover_animation(image, calibration, spills, path):
    """Write a looping animation highlighting the cells in *spills*, then optimize it."""
    # 3rd party
    from PIL import Image, ImageOps, ImageDraw

    base = image.convert('RGB')
    boxes = spilled_boxes(calibration, spills, base.size)
    mask = Image.new('L', base.size, 0)
    draw = ImageDraw.Draw(mask)
    for x0, y0, x1, y1 in boxes:
        draw.rectangle((x0, y0, x1 - 1, y1 - 1), fill=255)
    inverted = ImageOps.invert(base)
    half = ANIMATION_FRAMES // 2
    palette = _animation_palette(base, half)
    frames = []
    for index in range(ANIMATION_FRAMES):
        amount = abs(index - half) / half
        if amount:
            blended = Image.blend(base, inverted, amount)
            frame = Image.composite(blended, base, mask)
        else:
            frame = base
        frames.append(frame.quantize(
            palette=palette, dither=Image.Dither.NONE))
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        duration=int(round(100 / ANIMATION_FPS)) * 10,
        loop=0,
        disposal=2,
        optimize=False,
    )
    optimize_gif(path)
    return len(boxes)


def write_page_animation(crop_path, calibration, spills, path):
    """Write the evidence animation of one page from its cropped capture file."""
    write_spillover_animation(
        _load_capture(crop_path), calibration, spills, path)


def _write(text):
    sys.stdout.write(text)
    sys.stdout.flush()


def _park_cursor(term, row=0, column=0):
    _write(term.move(row, column))


def _focus_window(window_id):
    imaging.focus_window(window_id)


def _window_title(window_id):
    return imaging.window_title(window_id)


def _window_class(window_id):
    return imaging.window_class(window_id)


def _active_window():
    return imaging.active_window()


def _compositor_window(window_id):
    if macos.IS_MACOS:
        return None
    for candidate in (window_id, _active_window()):
        if candidate and ('Weston' in _window_title(candidate)
                          or 'Weston' in _window_class(candidate)):
            return candidate
    if _window_title(window_id) or _window_class(window_id):
        return None
    try:
        result = subprocess.run(
            ['xwininfo', '-root', '-tree'],
            capture_output=True, text=True, timeout=2, check=False)
    except (subprocess.TimeoutExpired, OSError):
        return None
    for line in result.stdout.splitlines():
        if 'Weston Compositor' in line:
            return line.split()[0]
    return None


def _hide_compositor_pointer(window_id):
    target = _compositor_window(window_id)
    if target is None:
        return None
    _focus_window(target)
    try:
        subprocess.run(
            ['xdotool', 'key', 'ctrl+shift+c'],
            capture_output=True, timeout=2, check=False)
    except (subprocess.TimeoutExpired, OSError):
        pass
    return target


def _same_pixels(first_path, second_path):
    """Return True when two captures show the same pixels."""
    # 3rd party
    from PIL import Image
    try:
        with Image.open(first_path) as first, Image.open(second_path) as second:
            return (first.size == second.size
                    and first.convert('RGB').tobytes()
                    == second.convert('RGB').tobytes())
    except OSError:
        return False


def _capture_settled(window_id, path, park, attempts=SETTLE_ATTEMPTS):
    """
    Capture until two frames agree, so a slow renderer is not measured mid-paint.

    The last frame is kept: a page that never settles is measured as it finally landed.
    """
    imaging.capture_window_raw(window_id, path, park=park)
    stem, suffix = os.path.splitext(path)
    settled_path = f'{stem}.settle{suffix}'
    try:
        for _attempt in range(attempts):
            time.sleep(SETTLE_DELAY)
            imaging.capture_window_raw(window_id, settled_path, park=park)
            same = _same_pixels(path, settled_path)
            os.replace(settled_path, path)
            if same:
                break
    finally:
        if os.path.exists(settled_path):
            os.unlink(settled_path)


def capture_page(window_id, path, refresh_window=None, term=None):
    """Capture the terminal window to *path* after a render pause."""
    last_error = None
    for attempt in range(2):
        try:
            with display_lock():
                compositor = _compositor_window(window_id)
                if compositor is None:
                    _focus_window(window_id)
                if term is not None:
                    term.get_location(timeout=2)
                time.sleep(0.25 + imaging.capture_delay())
                if compositor is not None:
                    _hide_compositor_pointer(window_id)
                _capture_settled(window_id, path, park=compositor is None)
            time.sleep(0.1)
            return window_id
        except (RuntimeError, OSError) as error:
            last_error = error
            if attempt == 0 and refresh_window is not None:
                new_window = refresh_window()
                if new_window:
                    window_id = new_window
                    time.sleep(0.5)
                    continue
            time.sleep(0.5)
    raise SpilloverError(str(last_error))


def run_calibration(term, window_id, temp_dir, refresh_window=None,
                    attempts=3, capture_path=None):
    """Render and measure a calibration page, retrying blank captures."""
    _write('\x1b[?25l')
    path = capture_path or os.path.join(temp_dir, 'calibration.png')
    last_error = None
    for attempt in range(attempts):
        _write(render_calibration(
            term.width, term.height, supports_truecolor(term)))
        time.sleep(0.4 + 0.4 * attempt)
        capture_page(window_id, path, refresh_window, term)
        try:
            return analyze_calibration(path, term.width, term.height)
        except SpilloverError as error:
            last_error = error
    raise last_error


def run_controls(term, window_id, temp_dir, calibration, refresh_window=None):
    """
    Draw control glyphs, returning their items, results, capture, rows, and calibration.

    The control page paints bars on every row, so it also reports how many rows the terminal shows,
    and it is the capture the cell pitch is fitted to.
    """
    items = []
    for index, candidate in enumerate(CONTROL_GRAPHEMES):
        column = START_COLUMN + index * COLUMN_STRIDE
        if column < term.width:
            items.append((0, column, candidate))
    _write(render_page(
        0, term.height, term.width,
        [(row, column, candidate.text)
         for row, column, candidate in items],
        supports_truecolor(term)))
    _park_cursor(term, 0, term.width - 1)
    path = os.path.join(temp_dir, 'controls.png')
    capture_page(window_id, path, refresh_window, term)

    # 3rd party
    from PIL import Image
    with Image.open(path) as image:
        rgb_image = image.convert('RGB')
    painted = max(1, visible_rows(rgb_image, calibration))
    calibration = refine_cell_width(path, calibration,
                                    row=max(1, painted // 2))
    results = analyze_page(
        rgb_image, calibration, items,
        reference_colors(rgb_image, calibration, row=painted - 1),
        reference_row=painted - 1)
    return (items, list(zip(CONTROL_GRAPHEMES, results)), path, painted,
            calibration)


def _color_text(color):
    return f'{color[0]},{color[1]},{color[2]}'


def control_page_report(calibration, path, items, controls):
    """Return a report describing how a control page was measured."""
    # 3rd party
    from PIL import Image
    with Image.open(path) as image:
        rgb_image = image.convert('RGB')
    rows = list(range(calibration.term_height))
    sampled = _cell_colors(rgb_image, calibration, rows)
    reference = sampled[calibration.term_height - 1]
    directory = os.path.dirname(path)
    try:
        kept = sorted(os.listdir(directory))
    except OSError:
        kept = []
    lines = [
        f'captures: {directory} {kept}',
        f'page {path} {rgb_image.size[0]}x{rgb_image.size[1]} '
        f'grid={calibration.term_width}x{calibration.term_height} '
        f'origin=({calibration.origin_x},{calibration.origin_y}) '
        f'cell={calibration.cell_width:.2f}x{calibration.cell_height:.2f}',
        ' '.join(_color_text(color) for color in reference[:8]),
    ]
    for row in rows[:4] + rows[-2:]:
        agree = sum(
            1 for column in range(calibration.term_width)
            if _color_distance(sampled[row][column], reference[column])
            <= COLOR_TOLERANCE)
        lines.append(
            f'row {row}: {agree}/{calibration.term_width} columns match the '
            f'reference row, {len(set(sampled[row]))} colors')
    flat_rows = [row for row in rows if len(set(sampled[row])) < 2]
    lines.append(f'rows without bars: {flat_rows[:8]} '
                 f'({len(flat_rows)} of {len(rows)})')
    for (row, column, candidate), control in zip(items, controls):
        result = control[1]
        span = list(range(max(0, column - 2),
                          min(calibration.term_width, column + 6)))
        lines.append(
            f'control {unicode_escape_string(candidate.text)} row={row} '
            f'column={column} left={result["left_cells"]} '
            f'right={result["right_cells"]} blank={result["blank"]} '
            f'shifted={result.get("shifted")}')
        lines.append(
            f'  row {row}:  ' + ' '.join(
                _color_text(sampled[row][cell]) for cell in span))
        lines.append(
            '  reference: ' + ' '.join(
                _color_text(reference[cell]) for cell in span))
    return '\n'.join(lines)


def _load_capture(path):
    # 3rd party
    from PIL import Image
    with Image.open(path) as image:
        return image.convert('RGB')


def cut_guard_rows(image, calibration, guard):
    """
    Return *image* without the *guard* rows, and *calibration* moved into it.

    The rows are spliced out rather than blanked, so the pointer pixels never reach the published
    page; every row below the guard moves up by the height of the cut.
    """
    if not guard:
        return image, calibration
    # 3rd party
    from PIL import Image

    start, count = guard
    top = int(round(calibration.origin_y + start * calibration.cell_height))
    bottom = int(round(
        calibration.origin_y + (start + count) * calibration.cell_height))
    top = max(0, min(top, image.height))
    bottom = max(top, min(bottom, image.height))
    if bottom <= top:
        return image, calibration
    kept = Image.new(image.mode, (image.width, image.height - (bottom - top)))
    kept.paste(image.crop((0, 0, image.width, top)), (0, 0))
    kept.paste(image.crop((0, bottom, image.width, image.height)), (0, top))
    return kept, calibration


def crop_to_grid(image, calibration, guard=None):
    """
    Return *image* cropped to the page grid, with *calibration* moved into the crop.

    A capture carries the window border, the terminal padding, and rows its pty reported but never
    showed.
    """
    width, height = image.size
    left = max(0, int(math.floor(calibration.origin_x)))
    top = max(0, int(math.floor(calibration.origin_y)))
    right = min(width, int(math.ceil(
        calibration.origin_x + calibration.term_width * calibration.cell_width)))
    bottom = min(height, int(math.ceil(
        calibration.origin_y + calibration.term_height * calibration.cell_height)))
    if right <= left or bottom <= top:
        return image, calibration
    cropped = image.crop((left, top, right, bottom))
    return cut_guard_rows(
        cropped,
        calibration._replace(origin_x=calibration.origin_x - left,
                             origin_y=calibration.origin_y - top),
        guard)


def analyze_capture(image_path, calibration, items, reference_row,
                    crop_path=None, guard=None):
    """
    Return per-item results and displaced rows for the page capture at *image_path*.

    Runs in a worker process and reads only the capture file, so the terminal paints the next page
    while this one is measured. The pitch is fitted to this page's own row.
    """
    rgb_image = _load_capture(image_path)
    refine_row = reference_row + guard[1] if guard else reference_row
    calibration = refine_cell_width_from_image(
        rgb_image, calibration, row=refine_row)
    rgb_image, calibration = crop_to_grid(rgb_image, calibration, guard)
    if crop_path:
        rgb_image.save(crop_path)
    reference = reference_colors(rgb_image, calibration, row=reference_row)
    displaced = shifted_rows(
        rgb_image, calibration, list(range(reference_row + 1)))
    return (analyze_page(rgb_image, calibration, items, reference,
                         reference_row=reference_row),
            sorted(displaced), calibration)


def scan_terminal(term, window_id, candidates, temp_dir,
                  evidence_dir=None, window_title=None, name_prefix=None,
                  pool=None, cursor_rows=0):
    """Scan *candidates* in the terminal behind *window_id*."""
    pool = pool or TaskPool()
    if evidence_dir:
        os.makedirs(evidence_dir, exist_ok=True)
    dump_dir = os.environ.get('UCS_SPILLOVER_DUMP')
    if dump_dir:
        os.makedirs(dump_dir, exist_ok=True)
    evidence_count = 0
    evidence_pages = []
    image_records = {}
    results = []
    errors = []
    shifted = []
    pending = []
    animation_jobs = []
    window_holder = [window_id]

    def refresh_window():
        if not window_title:
            return None
        found = imaging.find_own_window(window_title)
        if found:
            window_holder[0] = found
        return found

    calibration = run_calibration(
        term, window_holder[0], temp_dir, refresh_window)
    (control_items, controls, control_path, painted_rows,
     calibration) = run_controls(
        term, window_holder[0], temp_dir, calibration, refresh_window)
    painted_rows = max(2, painted_rows)
    guard = cursor_guard(term.height, cursor_rows)
    if guard and painted_rows - 1 - guard[1] < 1:
        guard = None
    ruler_row = painted_rows - 1
    if dump_dir:
        try:
            shutil.copyfile(control_path,
                            os.path.join(dump_dir, 'controls.png'))
        except OSError:
            pass
    for candidate, result in controls:
        if result['blank']:
            message = 'produced no visible pixels'
        elif result['left_cells'] or result['right_cells']:
            message = (f'spilled {result["left_cells"]} left and '
                       f'{result["right_cells"]} right')
        else:
            continue
        if candidate.label == 'ascii':
            print(control_page_report(
                calibration, control_path, control_items, controls),
                file=sys.stderr)
            raise SpilloverError(
                f'ASCII control glyph {message}, so the page grid is unusable')
        errors.append({
            'page': 0,
            'row': 0,
            'wchar': unicode_escape_string(candidate.text),
            'message': f'control glyph {message}',
        })

    rows, columns = page_layout(term.width, painted_rows, guard)
    reference_row = rows
    per_page = rows * columns
    n_pages = math.ceil(len(candidates) / per_page)

    for page_index in range(n_pages):
        start = page_index * per_page
        page = candidates[start:start + per_page]
        items = []
        for index, candidate in enumerate(page):
            row = index // columns
            column = START_COLUMN + (index % columns) * COLUMN_STRIDE
            items.append((row, column, candidate))

        _write(render_page(
            0, term.height, term.width,
            [(guard_row(row, guard), column, candidate.text)
             for row, column, candidate in items],
            supports_truecolor(term)))
        _park_cursor(term, 0, term.width - 1)
        image_path = os.path.join(temp_dir, f'page-{page_index:04d}.png')
        try:
            window_holder[0] = capture_page(
                window_holder[0], image_path, refresh_window, term)
        except SpilloverError as error:
            errors.append({
                'page': page_index,
                'row': -1,
                'wchar': '',
                'message': f'capture failed: {error}',
            })
            break

        rgb_image = _load_capture(image_path)
        if not page_has_bars(rgb_image, calibration, ruler_row):
            window_holder[0] = capture_page(
                window_holder[0], image_path, refresh_window, term)
            rgb_image = _load_capture(image_path)
        if not page_has_bars(rgb_image, calibration, ruler_row):
            if dump_dir:
                rgb_image.save(
                    os.path.join(dump_dir, f'page-{page_index:03d}-flat.png'))
            errors.append({
                'page': page_index,
                'row': -1,
                'wchar': '',
                'message': 'page capture showed one flat color',
            })
            continue
        if dump_dir:
            rgb_image.save(
                os.path.join(dump_dir, f'page-{page_index:03d}.png'))
        del rgb_image
        crop_path = os.path.join(temp_dir, f'page-{page_index:04d}-grid.png')
        pending.append((
            page_index, start, items, crop_path,
            pool.submit(analyze_capture, image_path, calibration, items,
                        reference_row, crop_path, guard,
                        label=f'page {page_index}')))

    for page_index, start, items, crop_path, future in pending:
        analysis, failure = pool.result(future, f'page {page_index}')
        if analysis is None:
            errors.append({
                'page': page_index,
                'row': -1,
                'wchar': '',
                'message': f'page analysis failed: {failure}',
            })
            continue
        page_results, displaced_rows, page_calibration = analysis
        displaced = set(displaced_rows)
        if reference_row in displaced:
            displaced = set(range(rows))
        shifted.extend(
            candidate.text for row, _column, candidate in items
            if row in displaced)
        spill_indexes = [
            index for index, result in enumerate(page_results)
            if result['left_cells'] or result['right_cells']]

        page_evidence = None
        if evidence_dir and spill_indexes:
            evidence_count += 1
            first_candidate = items[spill_indexes[0]][2]
            page_evidence = evidence_filename(
                evidence_count, ord(first_candidate.text[0]),
                name_prefix)
            categories = tuple(sorted({
                items[index][2].category for index in spill_indexes}))
            evidence_pages.append(
                (page_index, page_evidence, len(spill_indexes),
                 categories))
            spill_items = []
            page_spills = []
            for index in spill_indexes:
                row, column, candidate = items[index]
                row_result = page_results[index]
                advance = max(1, min(
                    candidate.advance or candidate.width, COLUMN_STRIDE))
                spill_items.append((
                    row, column, candidate,
                    row_result['left_cells'],
                    row_result['right_cells']))
                page_spills.append({
                    'wchar': unicode_escape_string(candidate.text),
                    'codepoints': [ord(char) for char in candidate.text],
                    'category': candidate.category,
                    'label': candidate.label,
                    'row': row,
                    'column': column,
                    'advance': advance,
                    'spill_left_cells': row_result['left_cells'],
                    'spill_right_cells': row_result['right_cells'],
                })
            animation_jobs.append(
                (page_evidence, crop_path, page_calibration,
                 tuple(spill_items)))
            image_records[page_evidence] = {
                'page': page_index,
                'spillovers': page_spills,
            }

        for index, (row, column, candidate) in enumerate(items):
            row_result = page_results[index]
            spilled = bool(
                row_result['left_cells'] or row_result['right_cells'])
            spill = Spillover(
                start + index, page_index, row, column, candidate,
                row_result['left_cells'], row_result['right_cells'],
                row_result['blank'],
                page_evidence if spilled else None)
            results.append(spill)

    kept = set(ranked_evidence_pages(image_records))
    for name, crop_path, page_calibration, spill_items in animation_jobs:
        if name not in kept:
            continue
        pool.submit(
            write_page_animation, crop_path, page_calibration, spill_items,
            os.path.join(evidence_dir, name), label=f'animation {name}')
    pool.collect()
    if evidence_dir and evidence_pages:
        results, image_records = prune_evidence(
            evidence_pages, evidence_dir, results, image_records)
    if evidence_dir and results:
        remove_stale_evidence(evidence_dir, image_records, name_prefix)

    return calibration, results, errors, image_records, shifted, painted_rows


def build_results(calibration, results, errors, n_candidates, images=None,
                  shifted=None, painted_rows=None, cursor_rows=0):
    """Return the YAML section describing a completed scan."""
    counts = spillover_statistics(results)
    by_kind = collections.defaultdict(list)
    tested_by_kind = collections.Counter(
        spillover_kind(result.candidate.category, result.candidate.label)
        for result in results)
    for result in results:
        if result.left_cells or result.right_cells:
            by_kind[spillover_kind(result.candidate.category,
                                   result.candidate.label)].append(
                (result.left_cells, result.right_cells))
    n_spillover = counts['graphemes_any']
    n_blank = sum(1 for result in results if result.blank)
    shifted = shifted or []
    if not painted_rows:
        painted_rows = calibration.term_height
    guard = cursor_guard(calibration.term_height, cursor_rows)
    if guard and painted_rows - 1 - guard[1] < 1:
        guard = None
    rows, columns = page_layout(calibration.term_width, painted_rows, guard)
    layout = {
        'left_cells': LEFT_CELLS,
        'column_stride': COLUMN_STRIDE,
        'start_column': START_COLUMN,
        'painted_rows': painted_rows,
        'rows_per_page': rows,
        'columns_per_page': columns,
        'items_per_page': rows * columns,
    }
    if guard:
        layout['cursor_center_rows'] = guard[1]
    return {
        'scanned_datetime': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
        'n_candidates': n_candidates,
        'n_tested': len(results),
        'n_spillover': n_spillover,
        'n_no_ink': n_blank,
        'n_shifted': len(shifted),
        'shifted_graphemes': [unicode_escape_string(text) for text in shifted],
        'spill_counts': counts,
        'spill_counts_by_kind': {
            kind: spillover_statistics_from_amounts(amounts)
            for kind, amounts in sorted(by_kind.items())},
        'spill_examples': spillover_examples(results),
        'n_tested_by_kind': dict(sorted(tested_by_kind.items())),
        'layout': layout,
        'calibration': {
            'origin_x': calibration.origin_x,
            'origin_y': calibration.origin_y,
            'cell_width_px': round(calibration.cell_width, 2),
            'cell_height_px': round(calibration.cell_height, 2),
            'term_width': calibration.term_width,
            'term_height': calibration.term_height,
        },
        'images': images or {},
        'errors': errors,
    }


class _ResultsDumper(yaml.SafeDumper):
    """Safe dumper used for the ``spillover_results`` section."""


def write_section(yaml_path, key, section):
    """Write *section* into *yaml_path* under *key*, in sorted position."""
    data = load_document(yaml_path)
    mode = os.stat(yaml_path).st_mode

    rebuilt = {}
    inserted = False
    for existing, value in data.items():
        if (not inserted and isinstance(existing, str)
                and existing > key):
            rebuilt[key] = section
            inserted = True
        if existing != key:
            rebuilt[existing] = value
    if not inserted:
        rebuilt[key] = section

    output = yaml.dump(
        rebuilt,
        Dumper=_ResultsDumper,
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
        width=1000,
    )
    payload = output.encode('utf-8')
    previous = os.path.getsize(yaml_path)
    # Terminal data reaches 2.7 MB; a rewrite that loses half of it means the parse dropped
    # sections, and replacing the file would destroy them.
    if previous > 1 << 17 and len(payload) * 2 < previous:
        raise SpilloverError(
            f'refusing to write {yaml_path}: {previous} bytes would become '
            f'{len(payload)}')
    directory = os.path.dirname(os.path.abspath(yaml_path))
    handle, temp_path = tempfile.mkstemp(
        prefix=f'.{key}-', suffix='.yaml', dir=directory)
    try:
        with os.fdopen(handle, 'wb') as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temp_path, mode)
        os.replace(temp_path, yaml_path)
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)


def write_results(yaml_path, section):
    """Write *section* into *yaml_path* as ``spillover_results``."""
    write_section(yaml_path, 'spillover_results', section)

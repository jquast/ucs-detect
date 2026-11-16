"""
Render one recent emoji and record the cell as ASCII art.

The font test draws a grapheme whose Unicode version is newer than most installed fonts carry,
captures the terminal window, and reduces the two cells it occupies to rows of ``.`` and ``X``. A
human can then read the shape and tell a real glyph from a tofu box or a missing glyph.  Results are
written to the terminal data YAML under ``font_test_results`` and are not published.
"""

# std imports
import os
import sys
import time

# local
from ucs_detect import fonts, spillover

#: Graphemes tried in order, newest Unicode emoji first.  Unifont 18.0.01 carries all of them.
FONT_TEST_GRAPHEMES = (
    ('\U0001FAEB', 'cracking face', '18.0'),
    ('\U0001FADD', 'pickle', '18.0'),
    ('\U0001FACC', 'monarch butterfly', '18.0'),
    ('\U0001FAE9', 'face with bags under eyes', '16.0'),
)

UNICODE_VERSION = '18.0'

#: Long established emoji drawn after the newest one.  It separates a terminal stack that cannot
#: handle a new codepoint from a font that has no glyph for it.
CONTROL_GRAPHEME = ('\U0001F600', 'grinning face', '1.0')

#: Terminal rows sampled per grapheme.
SAMPLED_CELLS = 2

#: ASCII grid size, per terminal cell.
ASCII_COLUMNS = 8
ASCII_ROWS = 16

#: Sum of channel differences above which a pixel counts as painted.
PAINTED_DISTANCE = 60

#: Fraction of an ASCII block that must be painted before the block is ``X``.
BLOCK_FRACTION = 0.3

TEST_ROW = 2
TEST_COLUMN = spillover.START_COLUMN

#: Blank painted row used to measure the background colors.  The last row is not used because a
#: Wayland client can be clipped below the grid size its pty reports.
REFERENCE_ROW = 0


def selected_grapheme():
    """Return the first font test grapheme, or ``UCS_FONT_TEST_CODEPOINT``."""
    override = os.environ.get('UCS_FONT_TEST_CODEPOINT')
    if override:
        codepoint = int(override.replace('U+', ''), 16)
        return (chr(codepoint), 'override', UNICODE_VERSION)
    return FONT_TEST_GRAPHEMES[0]


def _backgrounds(column, reference):
    colors = [spillover.GLYPH_BACKGROUND[0]]
    for index in (column, column + 1, column + 2):
        if 0 <= index < len(reference):
            colors.append(reference[index])
    return colors


def _is_painted(pixel, backgrounds):
    red, green, blue = pixel[:3]
    return all(abs(red - color[0]) + abs(green - color[1]) + abs(blue - color[2])
               > PAINTED_DISTANCE for color in backgrounds)


def _source_box(calibration, row, column, cells, image_size):
    x0 = int(round(calibration.origin_x + column * calibration.cell_width))
    x1 = int(round(calibration.origin_x
                   + (column + cells) * calibration.cell_width))
    y0 = int(round(calibration.origin_y + row * calibration.cell_height))
    y1 = int(round(calibration.origin_y + (row + 1) * calibration.cell_height))
    width, height = image_size
    return (max(0, min(x0, width - 1)), max(0, min(y0, height - 1)),
            max(1, min(x1, width)), max(1, min(y1, height)))


def cell_ascii(image, calibration, row=TEST_ROW, column=TEST_COLUMN,
               cells=SAMPLED_CELLS, reference=None):
    """Return ``(rows, painted_fraction, painted_color)`` for the grapheme at a cell."""
    if image.mode != 'RGB':
        image = image.convert('RGB')
    pixels = image.load()
    x0, y0, x1, y1 = _source_box(
        calibration, row, column, cells, image.size)
    if reference is None:
        reference = spillover.reference_colors(
            image, calibration, row=REFERENCE_ROW)
    backgrounds = _backgrounds(column, reference)
    columns = ASCII_COLUMNS * cells
    rows = []
    painted_total = 0
    sampled_total = 0
    painted_sum = [0, 0, 0]
    for grid_row in range(ASCII_ROWS):
        top = y0 + (y1 - y0) * grid_row // ASCII_ROWS
        bottom = max(top + 1, y0 + (y1 - y0) * (grid_row + 1) // ASCII_ROWS)
        line = []
        for grid_column in range(columns):
            left = x0 + (x1 - x0) * grid_column // columns
            right = max(
                left + 1, x0 + (x1 - x0) * (grid_column + 1) // columns)
            painted = 0
            total = 0
            for y in range(top, min(bottom, y1)):
                for x in range(left, min(right, x1)):
                    total += 1
                    pixel = pixels[x, y]
                    if _is_painted(pixel, backgrounds):
                        painted += 1
                        for channel in range(3):
                            painted_sum[channel] += pixel[channel]
            sampled_total += total
            painted_total += painted
            line.append('X' if total and painted / total >= BLOCK_FRACTION else '.')
        rows.append(''.join(line))
    fraction = painted_total / sampled_total if sampled_total else 0.0
    color = tuple(round(channel / painted_total) for channel in painted_sum) \
        if painted_total else (0, 0, 0)
    return rows, fraction, color


def grapheme_record(grapheme, ascii_rows, painted_fraction, painted_color):
    """Return one grapheme measurement mapping."""
    text, name, emoji_version = grapheme
    # local
    from ucs_detect.measure import unicode_escape_string
    return {
        'text': unicode_escape_string(text),
        'codepoint': f'U+{ord(text):04X}',
        'name': name,
        'emoji_version': emoji_version,
        'ink_fraction': round(painted_fraction, 3),
        'ink_color': list(painted_color),
        'monochrome': max(painted_color) - min(painted_color) <= 40,
        'ascii': ascii_rows,
    }


def build_section(calibration, measurements):
    """Return the ``font_test_results`` mapping from measured graphemes."""
    primary, control = measurements
    section = {
        'font_version': fonts.FONT_VERSION,
        'unicode_version': UNICODE_VERSION,
        'font_family': fonts.FONT_FAMILIES[0],
        'origin_x': calibration.origin_x,
        'origin_y': calibration.origin_y,
        'cell_width': round(calibration.cell_width, 2),
        'cell_height': round(calibration.cell_height, 2),
        'term_width': calibration.term_width,
        'term_height': calibration.term_height,
        'sampled_cells': SAMPLED_CELLS,
    }
    section.update(primary)
    section['grapheme'] = {
        key: primary[key]
        for key in ('text', 'codepoint', 'name', 'emoji_version')
    }
    section['control'] = control
    section['control']['grapheme'] = {
        key: control[key]
        for key in ('text', 'codepoint', 'name', 'emoji_version')
    }
    return section


def render_page(term_width, term_height, grapheme=None):
    """Return escapes that paint the page and draw the grapheme."""
    grapheme = grapheme or selected_grapheme()
    return spillover.render_page(
        0, term_height, term_width,
        [(TEST_ROW, TEST_COLUMN, grapheme[0])])


def measure_grapheme(term, window_id, temp_dir, calibration, grapheme,
                     capture_path=None, refresh_window=None):
    """Draw one grapheme and return its measurement mapping."""
    sys.stdout.write(render_page(term.width, term.height, grapheme))
    sys.stdout.flush()
    spillover._park_cursor(term, 0, term.width - 1)
    time.sleep(0.6)
    path = capture_path or os.path.join(temp_dir, 'font-test.png')
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    spillover.capture_page(window_id, path, refresh_window)

    # 3rd party
    from PIL import Image
    with Image.open(path) as image:
        image = image.convert('RGB')
        reference = spillover.reference_colors(
            image, calibration, row=REFERENCE_ROW)
        ascii_rows, fraction, color = cell_ascii(
            image, calibration, reference=reference)
    record = grapheme_record(grapheme, ascii_rows, fraction, color)
    record['reference'] = [
        list(item) for item in reference[TEST_COLUMN:TEST_COLUMN + 3]]
    return record


def scan(term, window_id, temp_dir, grapheme=None, refresh_window=None,
         capture_path=None):
    """Calibrate the terminal, draw each test grapheme, and return the measurements."""
    calibration_path = None
    if capture_path:
        calibration_path = (
            os.path.splitext(capture_path)[0] + '-calibration.png')
    calibration = spillover.run_calibration(
        term, window_id, temp_dir, refresh_window,
        capture_path=calibration_path)
    selected = grapheme or selected_grapheme()
    measurements = []
    for index, candidate in enumerate((selected, CONTROL_GRAPHEME)):
        path = None
        if capture_path:
            root, extension = os.path.splitext(capture_path)
            suffix = '' if index == 0 else '-control'
            path = f'{root}{suffix}{extension}'
        measurements.append(measure_grapheme(
            term, window_id, temp_dir, calibration, candidate,
            capture_path=path, refresh_window=refresh_window))
    return calibration, measurements


def write_results(yaml_path, section):
    """Write *section* into the terminal data YAML under ``font_test_results``."""
    spillover.write_section(yaml_path, 'font_test_results', section)

"""
Measure the default 16 colors a terminal renders.

The module paints one page: centered blocks for palette indices 0 through 15, each labelled with
``index:name``, on a contrasting page background.  It captures the page, samples each block, and
records the measured RGB values.

The default colors belong to the terminal theme, so they are reported, not scored.
"""

# std imports
import os
import math
import time
import collections

# local
from ucs_detect import spillover

#: Names blessed uses for the first 16 palette attributes, in palette order.
ANSI_COLOR_NAMES = (
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
    'bright_black',
    'bright_red',
    'bright_green',
    'bright_yellow',
    'bright_blue',
    'bright_magenta',
    'bright_cyan',
    'bright_white',
)

PAGE_FILENAME = 'colors-16.png'

#: Height in pixels of one color box in a summary palette strip.
STRIP_SWATCH_HEIGHT_PX = 32

#: Width in pixels of one color box in a summary palette strip, a square.
STRIP_SWATCH_WIDTH_PX = STRIP_SWATCH_HEIGHT_PX

#: Escape sequence that clears the page and returns the cursor home.
CLEAR = '\x1b[0m\x1b[2J\x1b[H'

RESET = '\x1b[0m'

#: RGB, ANSI, and 256 color fallbacks for the page background.
PAGE_BACKGROUND = ((48, 48, 48), '100', '238')

#: Longest label drawn next to a 16 color block.
SIXTEEN_LABEL_WIDTH = max(
    len(f'{index}:{name}')
    for index, name in enumerate(ANSI_COLOR_NAMES))

#: Cells reserved for one block, its gap, and its label.
SIXTEEN_GROUP_WIDTH = 2 + 1 + SIXTEEN_LABEL_WIDTH

SixteenLayout = collections.namedtuple(
    'SixteenLayout',
    ('columns', 'bands', 'block_width', 'block_height', 'group_width',
     'ruler_row', 'placements'))


class ColorError(RuntimeError):
    """Raised when a color page cannot be painted, captured, or measured."""


def rgb_hex(rgb):
    """Return *rgb* as a web color code."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


def _start_row(available, grid_height, guard):
    """Return the first content row of the block grid, clear of the pointer rows."""
    start = max(0, (available - grid_height) // 2)
    if not guard:
        return start
    band_start, band_count = guard
    band_end = band_start + band_count
    if start + grid_height <= band_start or start >= band_end:
        return start
    if band_end + grid_height <= available:
        return band_end
    if band_start - grid_height >= 0:
        return band_start - grid_height
    raise ColorError(
        f'{grid_height} color block rows do not fit around the pointer rows')


def sixteen_layout(term_width, term_height, guard=None):
    """Return the block, label, and ruler placement for the 16 color page."""
    if term_width < 1 or term_height < 2:
        raise ColorError('terminal is too small for the 16 color page')
    columns = min(4, max(1, term_width // SIXTEEN_GROUP_WIDTH))
    bands = math.ceil(len(ANSI_COLOR_NAMES) / columns)
    available = term_height - 1
    block_height = 2
    if bands * block_height > available:
        block_height = 1
    if bands * block_height > available:
        raise ColorError(
            f'{term_width}x{term_height} terminal cannot hold 16 labeled '
            f'color blocks')
    grid_width = columns * SIXTEEN_GROUP_WIDTH
    grid_height = bands * block_height
    start_column = max(0, (term_width - grid_width) // 2)
    start_row = _start_row(available, grid_height, guard)
    placements = []
    for index in range(len(ANSI_COLOR_NAMES)):
        band, slot = divmod(index, columns)
        placements.append((
            index,
            start_row + band * block_height,
            start_column + slot * SIXTEEN_GROUP_WIDTH,
        ))
    return SixteenLayout(columns, bands, 2, block_height, SIXTEEN_GROUP_WIDTH,
                         term_height - 1, tuple(placements))


def _move(row, column):
    return f'\x1b[{row + 1};{column + 1}H'


def _background_index(index):
    return f'\x1b[48;5;{index}m'


def _background_ansi(index):
    if index < 8:
        return f'\x1b[{40 + index}m'
    return f'\x1b[{100 + index - 8}m'


def _render_background(term_width, term_height):
    parts = []
    for row in range(term_height):
        parts.append(_move(row, 0))
        parts.append(spillover._sgr_background(*PAGE_BACKGROUND))
        parts.append(' ' * term_width)
        parts.append(RESET)
    return ''.join(parts)


def _render_ruler(term_width, ruler_row):
    parts = [_move(ruler_row, 0)]
    for column in range(term_width):
        parts.append(spillover._sgr_background(
            *spillover.BAR_COLORS[column % 2]))
        parts.append(' ')
    parts.append(RESET)
    return ''.join(parts)


def render_sixteen_page(term_width, term_height, layout=None):
    """Return escapes painting 16 labeled blocks and a ruler row."""
    layout = layout or sixteen_layout(term_width, term_height)
    parts = [CLEAR, _render_background(term_width, term_height)]
    for index, row, column in layout.placements:
        name = ANSI_COLOR_NAMES[index]
        label = f'{index}:{name}'
        label_column = column + layout.block_width + 1
        label = label[:max(0, term_width - label_column)]
        for block_row in range(layout.block_height):
            parts.append(_move(row + block_row, column))
            parts.append(_background_ansi(index))
            parts.append(_background_index(index))
            parts.append(' ' * layout.block_width)
            parts.append(RESET)
        if label:
            parts.append(_move(row, label_column))
            parts.append('\x1b[7m')
            parts.append(label)
            parts.append(RESET)
    parts.append(_render_ruler(term_width, layout.ruler_row))
    return ''.join(parts)


def sample_cell_color(image, calibration, row, column, margin=0.25):
    """Return the most common color inside one terminal cell."""
    if image.mode != 'RGB':
        image = image.convert('RGB')
    pixels = image.load()
    box = spillover._inner_box(
        spillover._cell_box(calibration, row, column, image.size), margin)
    counts = collections.Counter()
    for y in range(box[1], box[3]):
        for x in range(box[0], box[2]):
            counts[pixels[x, y][:3]] += 1
    if not counts:
        raise ColorError(f'no pixels in cell row {row} column {column}')
    return counts.most_common(1)[0][0]


def sample_block_color(image, calibration, row, column, width, height):
    """Return the most common color across a rectangular block of cells."""
    counts = collections.Counter()
    for block_row in range(height):
        for block_column in range(width):
            counts[sample_cell_color(
                image, calibration, row + block_row,
                column + block_column)] += 1
    return counts.most_common(1)[0][0]


def analyze_sixteen(image, calibration, layout):
    """Return the measured color of every 16 color block."""
    colors = []
    for index, row, column in layout.placements:
        rgb = sample_block_color(image, calibration, row, column,
                                 layout.block_width, layout.block_height)
        colors.append({
            'index': index,
            'name': ANSI_COLOR_NAMES[index],
            'rgb': list(rgb),
        })
    return colors


def _capture_page(term, window_id, path, calibration, ruler_row,
                  refresh_window):
    for attempt in range(2):
        spillover.capture_page(window_id, path, refresh_window, term)
        image = spillover._load_capture(path)
        if spillover.page_has_bars(image, calibration, ruler_row):
            return
        if attempt == 0:
            time.sleep(0.3)
    raise ColorError(f'page at {path} showed no ruler row')


def _save_page_crop(image, calibration, term_width, rows, directory,
                    guard=None):
    left = max(0, int(math.floor(calibration.origin_x)))
    top = max(0, int(math.floor(calibration.origin_y)))
    right = min(image.width, int(math.ceil(
        calibration.origin_x + term_width * calibration.cell_width)))
    bottom = min(image.height, int(math.ceil(
        calibration.origin_y + rows * calibration.cell_height)))
    if right <= left or bottom <= top:
        raise ColorError('capture is smaller than the terminal grid')
    page, _calibration = spillover.cut_guard_rows(
        image.crop((left, top, right, bottom)),
        calibration._replace(origin_x=calibration.origin_x - left,
                             origin_y=calibration.origin_y - top),
        guard)
    os.makedirs(directory, exist_ok=True)
    page.save(os.path.join(directory, PAGE_FILENAME))


def build_section(calibration, painted_rows, layout, colors):
    """Return the YAML section describing a completed color scan."""
    return {
        'scanned_datetime': time.strftime(
            '%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
        'painted_rows': painted_rows,
        'calibration': {
            'origin_x': calibration.origin_x,
            'origin_y': calibration.origin_y,
            'cell_width_px': round(calibration.cell_width, 2),
            'cell_height_px': round(calibration.cell_height, 2),
            'term_width': calibration.term_width,
            'term_height': calibration.term_height,
        },
        'sixteen': {
            'layout': {
                'columns': layout.columns,
                'bands': layout.bands,
                'block_width': layout.block_width,
                'block_height': layout.block_height,
                'group_width': layout.group_width,
                'ruler_row': layout.ruler_row,
            },
            'colors': colors,
        },
    }


def scan(term, window_id, temp_dir, capture_dir=None, refresh_window=None,
         cursor_rows=0):
    """Calibrate the terminal, draw the 16 color page, and measure the capture."""
    calibration = spillover.run_calibration(
        term, window_id, temp_dir, refresh_window)
    _items, _controls, _control_path, painted_rows, calibration = \
        spillover.run_controls(
            term, window_id, temp_dir, calibration, refresh_window)
    painted_rows = max(2, painted_rows)
    guard = spillover.cursor_guard(term.height, cursor_rows)
    if guard and guard[0] + guard[1] >= painted_rows - 1:
        guard = None
    layout = sixteen_layout(term.width, painted_rows, guard)
    spillover._write(render_sixteen_page(term.width, painted_rows, layout))
    spillover._park_cursor(term, 0, term.width - 1)
    path = os.path.join(temp_dir, PAGE_FILENAME)
    _capture_page(
        term, window_id, path, calibration, layout.ruler_row, refresh_window)
    page_calibration = spillover.refine_cell_width(
        path, calibration, row=layout.ruler_row, max_relative_error=0.10)
    image = spillover._load_capture(path)
    colors = analyze_sixteen(image, page_calibration, layout)
    if capture_dir:
        _save_page_crop(
            image, page_calibration, term.width,
            max(1, painted_rows - 1), capture_dir, guard)
    return (calibration,
            build_section(calibration, painted_rows, layout, colors),
            {'sixteen': path})


def write_results(yaml_path, section):
    """Write *section* into the terminal data YAML under ``color_results``."""
    spillover.write_section(yaml_path, 'color_results', section)


def write_swatch(path, rgb, size=1):
    """Write a *size* by *size* square of *rgb*."""
    # 3rd party
    from PIL import Image
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    Image.new('RGB', (size, size), tuple(rgb)).save(path)


def write_palette_strip(path, colors):
    """Write the palette side by side, one wide box per color."""
    # 3rd party
    from PIL import Image
    ordered = sorted(colors, key=lambda record: int(record.get('index', 0)))
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    image = Image.new(
        'RGB',
        (STRIP_SWATCH_WIDTH_PX * len(ordered), STRIP_SWATCH_HEIGHT_PX))
    for slot, record in enumerate(ordered):
        left = slot * STRIP_SWATCH_WIDTH_PX
        image.paste(
            tuple(record.get('rgb') or (0, 0, 0)),
            (left, 0, left + STRIP_SWATCH_WIDTH_PX, STRIP_SWATCH_HEIGHT_PX))
    image.save(path)

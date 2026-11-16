"""Detect a right to left layout by filling the left half of the screen and reading where it goes."""

# std imports
import os
import sys
import time
import collections

# local
from ucs_detect import imaging, spillover

#: ECMA-48 SCP selecting a right to left character path.
CHARACTER_PATH_RTL = '\x1b[2 k'

#: SCP with no parameter restores the terminal default.
CHARACTER_PATH_DEFAULT = '\x1b[ k'

#: Strong right to left character that sets the paragraph direction before the block.
RIGHT_TO_LEFT_LEAD = '\u05d0'

#: Character the block is painted with.
FILL = 'X'

#: Rows of the block.
ROWS = 3

#: Cells kept clear on each side of the split, so rounding cannot leak a column.
SPLIT_PAD = 2

#: Seconds a slow renderer is given to paint a page before it is captured.
PAGE_SETTLE = 0.5

#: Share of the painted pixels that must be on one side for the reading to count.
SIDE_SHARE = 0.8


def render_page(term_width, rtl):
    """Return a page whose left half holds one block of characters."""
    fill = FILL * max(1, term_width // 2 - 1 - SPLIT_PAD)
    if rtl:
        fill = RIGHT_TO_LEFT_LEAD + fill
    parts = [spillover.PAGE_CLEAR, CHARACTER_PATH_DEFAULT]
    for row in range(ROWS):
        parts.append(f'\x1b[{row + 1};1H')
        if rtl:
            parts.append(CHARACTER_PATH_RTL)
        parts.append(fill)
    return ''.join(parts)


def painted_sides(image, calibration):
    """Return ``(left, right)`` painted pixels outside the padded split band."""
    pixels = image.load()
    background = collections.Counter(
        pixels[x, y][:3]
        for y in range(0, image.height, 4)
        for x in range(0, image.width, 4)).most_common(1)[0][0]
    half = calibration.term_width // 2
    left_edge = calibration.origin_x + (half - SPLIT_PAD) * calibration.cell_width
    right_edge = calibration.origin_x + (half + SPLIT_PAD) * calibration.cell_width
    left = right = 0
    for y in range(0, image.height, 2):
        for x in range(0, image.width, 2):
            red, green, blue = pixels[x, y][:3]
            difference = (abs(red - background[0]) + abs(green - background[1])
                   + abs(blue - background[2]))
            if difference <= 90:
                continue
            if x < left_edge:
                left += 1
            elif x > right_edge:
                right += 1
    return left, right


def build_results(counts, errors):
    """Return the YAML section of a completed probe."""
    control_left, control_right = counts.get('control', (0, 0))
    requested_left, requested_right = counts.get('requested', (0, 0))
    control_total = control_left + control_right
    requested_total = requested_left + requested_right
    if not control_total or not requested_total:
        verdict = None
    elif control_left / control_total < SIDE_SHARE:
        verdict = None
    else:
        verdict = requested_right / requested_total >= SIDE_SHARE
    return {
        'scanned_datetime': time.strftime(
            '%Y-%m-%d %H:%M:%S UTC', time.gmtime()),
        'supported': verdict,
        'control_left': (round(control_left / control_total, 3)
                         if control_total else None),
        'requested_right': (round(requested_right / requested_total, 3)
                            if requested_total else None),
        'errors': errors,
    }


def _write(text):
    sys.stdout.write(text)
    sys.stdout.flush()


def scan_terminal(term, window_id, temp_dir, window_title=None):
    """Probe *term* and return its YAML section."""
    def refresh_window():
        return imaging.find_own_window(window_title) if window_title else None

    calibration = spillover.run_calibration(
        term, window_id, temp_dir, refresh_window)
    counts = {}
    errors = []
    for name, rtl in (('control', False), ('requested', True)):
        _write(render_page(term.width, rtl))
        _write(term.move(0, 0))
        time.sleep(PAGE_SETTLE)
        path = os.path.join(temp_dir, f'bidi-{name}.png')
        try:
            window_id = spillover.capture_page(
                window_id, path, refresh_window, term)
        except spillover.SpilloverError as error:
            errors.append({'capture': name, 'message': str(error)})
            continue
        # 3rd party
        from PIL import Image
        with Image.open(path) as image:
            cropped, moved = spillover.crop_to_grid(
                image.convert('RGB'), calibration)
        counts[name] = painted_sides(cropped, moved)
    return build_results(counts, errors)


def write_results(yaml_path, section):
    """Write *section* into *yaml_path* as ``bidi_results``."""
    spillover.write_section(yaml_path, 'bidi_results', section)

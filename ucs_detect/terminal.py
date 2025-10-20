import time
import functools
import sys

import blessed
import ucs_detect
import ucs_detect.table_wide


# Get all DEC Private Mode constants from blessed for querying
SCREEN_RATIOS = [(4, 3), (16, 9), (16, 10), (21, 9), (32, 9)]
DEFAULT_FONT_WIDTH = 640 // 80
DEFAULT_FONT_HEIGHT = 400 // 25


def _get_all_dec_private_mode_numbers():
    """Extract all uppercase DEC Private Mode constants from blessed.DecPrivateMode."""
    from blessed.dec_modes import DecPrivateMode
    return sorted([
        getattr(DecPrivateMode, attr)
        for attr in dir(DecPrivateMode)
        if attr.isupper() and isinstance(getattr(DecPrivateMode, attr), int) and getattr(DecPrivateMode, attr) > 0
    ])


def _nearest_fraction(numerator: int, denominator: int, fractions: list[tuple[int, int]]):
    """
    return nearest fraction of 'fractions', given a numerator and denominator
    """
    closest_pair = None
    min_difference = float('inf')

    for tgt_numerator, tgt_denominator in fractions:
        difference = abs(numerator / denominator - tgt_numerator / tgt_denominator)
        if difference < min_difference:
            min_difference = difference
            closest_pair = (tgt_numerator, tgt_denominator)

    return closest_pair
    

def get_tty_size(term, writer):
    # parse TIOCGWINSZ for terminal size and initial pixel_width and height
    # (usually 0, there), the default blessed attributes use just this part of
    # the tty. blessed does a fallback to environment variables LINES and
    # COLUMNS, which is traditional for non-ttys
    return {
        'width': term.width,
        'height': term.height,
        'pixels_width': term.pixel_width,
        'pixels_height': term.pixel_height,
    }


def maybe_determine_dec_modes(term):
    # Query all modes with a 1-second timeout; note that 1-second timeout is
    # only incurred for first query, all remaining are in error/unsupported
    # state
    modes_to_query = list(_get_all_dec_private_mode_numbers())
    result = {'modes': {}}
    for mode_num in modes_to_query:
        response = term.get_dec_mode(mode_num, timeout=1.0)

        # Only include modes that were successfully *queried*,
        if not response.failed:
            result['modes'][mode_num] = {
                'value': response.value,
                'value_description': str(response),
                'mode_description': response.description,
                'mode_name': response.mode.name,
                'supported': response.supported,
                'enabled': response.enabled,
                'changeable': response.changeable,
            }
    return result

def maybe_determine_da_and_sixel(term):
    # Parse "primary device attributes" using blessed's get_device_attributes
    result = {}
    da = term.get_device_attributes(timeout=1.0)

    if da is not None:
        result['device_attributes'] = {
            'service_class': da.service_class,
            'extensions': sorted(da.extensions),
        }
    result['sixel'] = term.does_sixel(timeout=1.0)
    return result

def maybe_determine_software(term, writer):
    result = {}
    sv = term.get_software_version(timeout=1.0)
    if sv is not None:
        result['software_name'] = sv.name
        if sv.version:
            result['software_version'] = sv.version
    return result

def maybe_determine_cell_size(term, writer):
    # if cell_height and width is already determined, do not perform interrogation
    cell_height, cell_width = term.get_cell_height_and_width(timeout=1.0)
    if cell_height != -1 and cell_width != -1:
        return {"cell_height": cell_height, "cell_width": cell_width}
    return 

def maybe_determine_pixel_size(term, writer):
    # use "sixel calculation" from blessed, which uses some heuristics
    pixel_height, pixel_width = term.get_sixel_height_and_width(timeout=1.0)
    if pixel_height > 0 and pixel_width > 0:
        return {"pixels_height": pixel_height, "pixels_width": pixel_width}
    return {}

def maybe_determine_screen_ratio(attrs):    
    # uses only pixel-width and height when available, because font size is not
    # reliably known, though we could also provide some kind of textual aspect
    # ratio, which is already a bit difficult to grok in any common terms,
    # anyway, since the font size itself varies across systems that don't report
    # it, so we don't report it either
    MATCHING_SCREEN_RATIOS = {'4:3': 'VGA', '16:9': 'HD', '16:10': 'WSXGA', '21:9': 'UWHD', '32:9': 'WQHD'}
    if attrs.get('pixels_width', 0) and attrs.get('pixels_height', 0):
        screen_ratio = ':'.join(map(str, _nearest_fraction(attrs['pixels_width'], attrs['pixels_height'], SCREEN_RATIOS)))
        screen_ratio_name = MATCHING_SCREEN_RATIOS[screen_ratio]
        return {'screen_ratio': screen_ratio, 'screen_ratio_name': screen_ratio_name}
    return {}

def do_terminal_detection(all_modes=False):
    writer = functools.partial(print, end="", flush=True, file=sys.stderr)
    term = blessed.Terminal()
    attrs = {'ttype': term.kind, 'number_of_colors': term.number_of_colors }
    attrs.update(get_tty_size(term, writer))
    attrs.update(maybe_determine_dec_modes(term))
    attrs.update(maybe_determine_da_and_sixel(term))
    attrs.update(maybe_determine_software(term, writer))
    attrs.update(maybe_determine_cell_size(term, writer))
    attrs.update(maybe_determine_pixel_size(term, writer))
    attrs.update(maybe_determine_screen_ratio(attrs))
    return attrs

if __name__ == '__main__':
    result = do_terminal_detection()
    import json
    json.dump(result, sys.stdout, indent=4, sort_keys=True)

import time
import functools
import sys
import uuid
import contextlib

import blessed
import wcwidth
import ucs_detect
import ucs_detect.table_wide


# Get all DEC Private Mode constants from blessed for querying
SCREEN_RATIOS = [(4, 3), (16, 9), (16, 10), (21, 9), (32, 9)]
DEFAULT_FONT_WIDTH = 640 // 80
DEFAULT_FONT_HEIGHT = 400 // 25


def get_latest_unicode_version():
    """
    Get the highest non-dotted Unicode version number available in wcwidth.

    For example, if wcwidth supports up to 17.0.0, this returns 17.
    """
    from ucs_detect.table_wide import WIDE_CHARACTERS
    all_versions = [ver for ver, _ in WIDE_CHARACTERS]
    if not all_versions:
        return 9
    # Get the highest version and extract major version number
    latest = max(all_versions, key=lambda v: wcwidth._wcversion_value(v))
    major_version = int(latest.split('.')[0])
    return major_version


def emit_osc_1337_unicode_version(writer, version):
    """
    Emit OSC 1337 escape sequence to set terminal Unicode version.

    This attempts to switch the terminal's Unicode version dynamically using
    the iTerm2/WezTerm proprietary escape sequence. Terminals that don't support
    this will simply ignore it.
    """
    writer(f"\x1b]1337;UnicodeVersion={version}\x07")


def emit_osc_1337_push(writer, label):
    """
    Push the current Unicode version onto the stack with a label.

    This allows restoring the terminal's Unicode version later using pop.
    """
    writer(f"\x1b]1337;UnicodeVersion=push {label}\x07")


def emit_osc_1337_pop(writer, label):
    """
    Pop Unicode version from stack until the specified label is found.

    This restores the terminal to a previously pushed Unicode version.
    """
    writer(f"\x1b]1337;UnicodeVersion=pop {label}\x07")


class osc_1337_unicode_version_context:
    """
    Context manager for OSC 1337 Unicode version push/pop.

    Pushes current Unicode version on entry and pops it on exit.
    """
    def __init__(self, writer):
        self.writer = writer
        self.label = str(uuid.uuid4())

    def __enter__(self):
        emit_osc_1337_push(self.writer, self.label)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        emit_osc_1337_pop(self.writer, self.label)
        return False


class grapheme_clustering_mode_context:
    """
    Context manager for DEC mode 2027 (GRAPHEME_CLUSTERING).

    Enables grapheme clustering on entry and restores original state on exit.
    """
    def __init__(self, term):
        self.term = term

    def __enter__(self):
        from blessed.dec_modes import DecPrivateMode
        self.term._stream.write(self.term.set_dec_mode(DecPrivateMode.GRAPHEME_CLUSTERING))
        self.term._stream.flush()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        from blessed.dec_modes import DecPrivateMode
        self.term._stream.write(self.term.reset_dec_mode(DecPrivateMode.GRAPHEME_CLUSTERING))
        self.term._stream.flush()
        return False


@contextlib.contextmanager
def osc_1337_for_version(writer, version_str, enabled):
    """
    Context manager that pushes, sets Unicode version, then pops on exit.

    For each Unicode version being tested, this pushes the current terminal
    Unicode version, sets it to the test version, yields for testing,
    then pops back to the previous version.
    """
    if enabled:
        label = str(uuid.uuid4())
        emit_osc_1337_push(writer, label)
        ver_major = int(version_str.split('.')[0]) if '.' in version_str else int(version_str)
        emit_osc_1337_unicode_version(writer, ver_major)
        yield
        emit_osc_1337_pop(writer, label)
    else:
        yield


def maybe_grapheme_clustering_mode(term, enabled):
    """
    Return grapheme clustering context manager if enabled, otherwise nullcontext.

    This allows conditional use of DEC mode 2027 (GRAPHEME_CLUSTERING).
    """
    if enabled:
        return grapheme_clustering_mode_context(term)
    return contextlib.nullcontext()


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
    return {}

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

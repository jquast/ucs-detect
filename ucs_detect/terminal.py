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


def maybe_grapheme_clustering_mode(term):
    return term.dec_modes_enabled(term.DecPrivateMode.GRAPHEME_CLUSTERING, timeout=1)


def _get_all_dec_private_mode_numbers(term):
    """Extract all uppercase DEC Private Mode constants from blessed.DecPrivateMode."""
    return sorted([
        getattr(term.DecPrivateMode, attr)
        for attr in dir(term.DecPrivateMode)
        if attr.isupper() and isinstance(getattr(term.DecPrivateMode, attr), int) and getattr(term.DecPrivateMode, attr) > 0
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
    modes_to_query = list(_get_all_dec_private_mode_numbers(term))
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

def _read_dcs_or_plain_response(term, timeout=0.5):
    """
    Read a response that might be plain text or a DCS sequence.

    Handles both:
    - Plain answerback: ">|mintty 3.8.0"
    - DCS answerback: "ESC P >|mintty 3.8.0 ESC \"

    Returns the extracted content without DCS wrapper.
    """
    response = term.flushinp(timeout=timeout)
    if not response:
        return ''

    # Check if response contains DCS sequence: ESC P ... ESC \ or ESC P ... ST
    # DCS starts with ESC P (\x1bP) and ends with ESC \ (\x1b\x5c) or ST (\x9c)
    if '\x1bP' in response:
        # Extract content between DCS start and end
        start_idx = response.find('\x1bP')
        # Look for ESC \ terminator
        end_idx = response.find('\x1b\\', start_idx)
        if end_idx == -1:
            # Look for ST terminator
            end_idx = response.find('\x9c', start_idx)

        if end_idx > start_idx:
            # Extract DCS content (skip ESC P, stop before terminator)
            dcs_content = response[start_idx + 2:end_idx]
            return dcs_content.strip()
        else:
            # No terminator found, return content after DCS start
            return response[start_idx + 2:].strip()

    # Not a DCS, return as-is
    return response.strip()

def maybe_determine_software(term, writer):
    result = {}
    sv = term.get_software_version(timeout=1.0)
    if sv is not None:
        result['software_name'] = sv.name
        if sv.version:
            result['software_version'] = sv.version
    else:
        # XTVERSION failed, try ENQ (answerback) sequence as fallback
        # Write ENQ directly to terminal stream instead of through writer
        if term.stream:
            term.stream.write('\x05')
            term.stream.flush()
        else:
            # Fallback to stderr if no stream
            sys.stderr.write('\x05')
            sys.stderr.flush()

        # Small delay to allow answerback response to arrive
        time.sleep(0.1)
        response = _read_dcs_or_plain_response(term, timeout=0.5)
        if response:
            # Parse answerback response to extract software name and version
            if response.startswith('>|'):
                # remove this answerback prefix sometimes used
                response = response[len('>|'):]
            result['software_name'] = response

            # Try to split into name and version
            # Format: "SoftwareName Version.Number"
            parts = response.split()
            if len(parts) >= 2:
                # Check if last part looks like a version number (contains digits and dots)
                last_part = parts[-1]
                if any(c.isdigit() for c in last_part):
                    # Last part is (maybe) a version number
                    result['software_name'] = ' '.join(parts[:-1])
                    result['software_version'] = last_part

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

def maybe_determine_colors(term, writer):
    """
    Query terminal foreground and background colors.

    Uses blessed Terminal.get_fgcolor() and get_bgcolor() to determine the
    terminal's default foreground and background colors.

    Returns dictionary with color information as RGB lists and hex strings.
    """
    result = {}

    # Get foreground color
    r, g, b = term.get_fgcolor()
    if (r, g, b) != (-1, -1, -1):
        result['foreground_color_rgb'] = [r, g, b]
        result['foreground_color_hex'] = f"#{r:04x}{g:04x}{b:04x}"

    # Get background color
    r, g, b = term.get_bgcolor()
    if (r, g, b) != (-1, -1, -1):
        result['background_color_rgb'] = [r, g, b]
        result['background_color_hex'] = f"#{r:04x}{g:04x}{b:04x}"

    return result

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
    attrs.update(maybe_determine_colors(term, writer))
    return attrs

if __name__ == '__main__':
    result = do_terminal_detection()
    import json
    json.dump(result, sys.stdout, indent=4, sort_keys=True)

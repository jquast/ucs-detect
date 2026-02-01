import contextlib
import re
import time
import functools
import sys
import warnings

import blessed


SCREEN_RATIOS = [(4, 3), (16, 9), (16, 10), (21, 9), (32, 9)]


def make_terminal(fallback_kind="xterm", **kwargs):
    """Create a :class:`blessed.Terminal`, falling back to *fallback_kind*
    when ``curses.setupterm()`` fails for the current ``$TERM``."""
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        term = blessed.Terminal(**kwargs)
    if any("setupterm" in str(w.message) for w in caught):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            term = blessed.Terminal(kind=fallback_kind, **kwargs)
    return term


@contextlib.contextmanager
def _status(writer, term, label, bg_rgb=None):
    """Display a status line, hiding test output when bg_rgb is set."""
    writer(f'\rucs-detect: {label} ..{term.clear_eol}')
    if bg_rgb is not None:
        writer(term.color_rgb(*bg_rgb))
    try:
        yield
    finally:
        if bg_rgb is not None:
            writer(term.normal)
        writer(f'\r{term.clear_eol}')



def maybe_grapheme_clustering_mode(term, timeout=1.0):
    return term.dec_modes_enabled(term.DecPrivateMode.GRAPHEME_CLUSTERING, timeout=timeout)


def _get_all_dec_private_mode_numbers(term):
    """Extract all uppercase DEC Private Mode constants from blessed.DecPrivateMode."""
    return sorted([
        getattr(term.DecPrivateMode, attr)
        for attr in dir(term.DecPrivateMode)
        if attr.isupper() and isinstance(getattr(term.DecPrivateMode, attr), int) and getattr(term.DecPrivateMode, attr) > 0
        ])


def _nearest_fraction(numerator: int, denominator: int, fractions: list[tuple[int, int]]):
    """Return nearest fraction from *fractions* to numerator/denominator."""
    target = numerator / denominator
    return min(fractions, key=lambda f: abs(target - f[0] / f[1]))


def get_tty_size(term, writer):
    return {
            'width': term.width,
            'height': term.height,
            'pixels_width': term.pixel_width,
            'pixels_height': term.pixel_height,
            }


NOTABLE_DEC_MODES = [
    2004,  # Bracketed Paste
    2026,  # Synchronized Output
    2027,  # Grapheme Clustering
    1004,  # Focus Events
    1006,  # Mouse SGR
]


def maybe_determine_dec_modes(term, writer, all_modes=False, bg_rgb=None,
                              timeout=1.0, cps_tracker=None):
    """Query DEC private modes (notable only, or all when *all_modes* is set)."""
    if all_modes:
        modes_to_query = list(_get_all_dec_private_mode_numbers(term))
    else:
        modes_to_query = list(NOTABLE_DEC_MODES)
    hide = term.color_rgb(*bg_rgb) if bg_rgb is not None else ''
    unhide = term.normal if bg_rgb is not None else ''
    result = {'modes': {}}
    n_ok = 0
    ok_elapsed = 0.0
    for mode_num in modes_to_query:
        writer(f'\rucs-detect: DEC mode {mode_num} ..{term.clear_eol}{hide}')
        t0 = time.monotonic()
        response = term.get_dec_mode(mode_num, timeout=timeout)
        elapsed = time.monotonic() - t0
        if not response.failed:
            n_ok += 1
            ok_elapsed += elapsed
            result['modes'][mode_num] = {
                    'value': response.value,
                    'value_description': str(response),
                    'mode_description': response.description,
                    'mode_name': response.mode.name,
                    'supported': response.supported,
                    'enabled': response.enabled,
                    'changeable': response.changeable,
                    }
        writer(unhide)
    if cps_tracker and n_ok:
        cps_tracker.update(n_ok, ok_elapsed)
    writer(f'\r{term.clear_eol}')
    return result

def maybe_determine_da_and_sixel(term, timeout=1.0):
    result = {}
    da = term.get_device_attributes(timeout=timeout)

    if da is not None:
        result['device_attributes'] = {
                'service_class': da.service_class,
                'extensions': sorted(da.extensions),
                }
    result['sixel'] = term.does_sixel(timeout=timeout)
    return result

def _read_dcs_or_plain_response(term, timeout=0.5):
    """Read a response, stripping any DCS wrapper."""
    response = term.flushinp(timeout=timeout)
    if not response:
        return ''

    if '\x1bP' in response:
        start_idx = response.find('\x1bP')
        end_idx = response.find('\x1b\\', start_idx)
        if end_idx == -1:
            end_idx = response.find('\x9c', start_idx)

        if end_idx > start_idx:
            return response[start_idx + 2:end_idx].strip()
        return response[start_idx + 2:].strip()

    return response.strip()

def _try_decode_da3_name(name):
    """Decode DA3-style semicolon-separated ASCII values to a string.

    SyncTERM's CTerm engine is the only known terminal to identify itself
    this way, encoding its name and version as decimal ASCII codepoints
    in a DA3-format response (e.g. ``CSI = 67;84;101;114;109;1;323 c``
    decodes to "CTerm" version "1.323").

    :rtype: tuple of (name, version) or None
    """
    if not name or ';' not in name:
        return None
    # strip CSI prefix (ESC[= or ESC[) and trailing 'c'
    raw = name
    for prefix in ('\x1b[=', '\x1b['):
        if raw.startswith(prefix):
            raw = raw[len(prefix):]
            break
    raw = raw.rstrip('c').strip()
    parts = raw.split(';')
    try:
        values = [int(p) for p in parts]
    except ValueError:
        return None
    # split into printable ASCII name codepoints and remaining version params
    name_chars = []
    version_parts = []
    for i, v in enumerate(values):
        if 32 <= v < 127:
            name_chars.append(chr(v))
        else:
            version_parts = values[i:]
            break
    if not name_chars:
        return None
    decoded_name = ''.join(name_chars)
    decoded_version = '.'.join(str(v) for v in version_parts) if version_parts else ''
    return decoded_name, decoded_version


def maybe_determine_software(term, writer, timeout=1.0):
    result = {}
    sv = term.get_software_version(timeout=timeout)
    if sv is not None:
        name = sv.name
        # decode DA3-style ASCII-encoded name (only SyncTERM/CTerm is
        # known to respond this way)
        decoded = _try_decode_da3_name(name)
        if decoded:
            name, version = decoded
            result['software_name'] = name
            if version:
                result['software_version'] = version
        else:
            result['software_name'] = name
            if sv.version:
                result['software_version'] = sv.version
    else:
        # XTVERSION failed, try ENQ (answerback) as fallback
        if term.stream:
            term.stream.write('\x05')
            term.stream.flush()
        else:
            # Fallback to stderr if no stream
            sys.stderr.write('\x05')
            sys.stderr.flush()

        time.sleep(0.1)
        response = _read_dcs_or_plain_response(term, timeout=0.5)
        if response:
            if response.startswith('>|'):
                response = response[2:]

            # check for DA3-style ASCII-encoded name (only SyncTERM/CTerm
            # is known to respond this way)
            decoded = _try_decode_da3_name(response)
            if decoded:
                result['software_name'] = decoded[0]
                if decoded[1]:
                    result['software_version'] = decoded[1]
            else:
                result['software_name'] = response
                parts = response.split()
                if len(parts) >= 2:
                    last_part = parts[-1]
                    if any(c.isdigit() for c in last_part):
                        result['software_name'] = ' '.join(parts[:-1])
                        result['software_version'] = last_part

    return result

def maybe_determine_cell_size(term, writer, timeout=1.0):
    cell_height, cell_width = term.get_cell_height_and_width(timeout=timeout)
    if cell_height != -1 and cell_width != -1:
        return {"cell_height": cell_height, "cell_width": cell_width}
    return {}

def maybe_determine_pixel_size(term, writer, timeout=1.0):
    pixel_height, pixel_width = term.get_sixel_height_and_width(timeout=timeout)
    if pixel_height > 0 and pixel_width > 0:
        return {"pixels_height": pixel_height, "pixels_width": pixel_width}
    return {}

def maybe_determine_screen_ratio(attrs):
    MATCHING_SCREEN_RATIOS = {'4:3': 'VGA', '16:9': 'HD', '16:10': 'WSXGA', '21:9': 'UWHD', '32:9': 'WQHD'}
    if attrs.get('pixels_width', 0) and attrs.get('pixels_height', 0):
        screen_ratio = ':'.join(map(str, _nearest_fraction(attrs['pixels_width'], attrs['pixels_height'], SCREEN_RATIOS)))
        screen_ratio_name = MATCHING_SCREEN_RATIOS[screen_ratio]
        return {'screen_ratio': screen_ratio, 'screen_ratio_name': screen_ratio_name}
    return {}

def maybe_determine_colors(term, writer):
    """Query terminal foreground and background colors."""
    result = {}

    r, g, b = term.get_fgcolor()
    if (r, g, b) != (-1, -1, -1):
        result['foreground_color_rgb'] = [r, g, b]
        result['foreground_color_hex'] = f"#{r:04x}{g:04x}{b:04x}"

    r, g, b = term.get_bgcolor()
    if (r, g, b) != (-1, -1, -1):
        result['background_color_rgb'] = [r, g, b]
        result['background_color_hex'] = f"#{r:04x}{g:04x}{b:04x}"

    return result

def maybe_determine_kitty_keyboard(term, timeout=1.0):
    """Query Kitty keyboard protocol support."""
    result = {}
    kb_state = term.get_kitty_keyboard_state(timeout=timeout)
    if kb_state is not None:
        result['kitty_keyboard'] = {
            'disambiguate': kb_state.disambiguate,
            'report_events': kb_state.report_events,
            'report_alternates': kb_state.report_alternates,
            'report_all_keys': kb_state.report_all_keys,
            'report_text': kb_state.report_text,
        }
    return result


def echo(term, data):
    """Write raw data to the terminal stream and flush."""
    term.stream.write(data)
    term.stream.flush()


def _hex_encode(name):
    """Hex-encode a capability name for XTGETTCAP."""
    return name.encode('ascii').hex()


def _hex_decode(hex_str):
    """Decode a hex-encoded string from an XTGETTCAP response."""
    try:
        return bytes.fromhex(hex_str).decode('ascii', errors='replace')
    except (ValueError, UnicodeDecodeError):
        return hex_str


def maybe_determine_xtgettcap(term, timeout=1.0, cursor_report_delay_ms=0):
    """Query terminal capabilities via XTGETTCAP (DCS+q)."""
    from ucs_detect.table_xtgettcap import XTGETTCAP_CAPABILITIES

    result = {'xtgettcap': {'supported': False, 'capabilities': {}}}

    for capname, _desc in XTGETTCAP_CAPABILITIES:
        hex_name = _hex_encode(capname)
        echo(term, f'\x1bP+q{hex_name}\x1b\\')

    if cursor_report_delay_ms:
        time.sleep(cursor_report_delay_ms / 1000.0)
    raw = term.flushinp(timeout=timeout)
    if not raw:
        return result

    result['xtgettcap']['supported'] = True

    for match in re.finditer(r'\x1bP([01])\+r([0-9a-fA-F]+)(?:=([0-9a-fA-F]*))?\x1b\\', raw):
        success = match.group(1) == '1'
        cap_hex = match.group(2)
        val_hex = match.group(3)

        cap_name = _hex_decode(cap_hex)
        if success and val_hex is not None:
            result['xtgettcap']['capabilities'][cap_name] = _hex_decode(val_hex)
        elif success:
            result['xtgettcap']['capabilities'][cap_name] = True

    return result


def maybe_determine_kitty_graphics(term, timeout=1.0, cursor_report_delay_ms=0):
    """Detect Kitty graphics protocol support."""
    echo(term, '\x1b_Gi=31,s=1,v=1,a=q,t=d,f=24;AAAA\x1b\\')
    if cursor_report_delay_ms:
        time.sleep(cursor_report_delay_ms / 1000.0)
    raw = term.flushinp(timeout=timeout)
    supported = raw is not None and 'OK' in raw
    return {'kitty_graphics': supported}


def maybe_determine_iterm2_features(term, timeout=1.0, cursor_report_delay_ms=0):
    """Query iTerm2 feature reporting protocol."""
    result = {'iterm2_features': {'supported': False, 'features': {}}}
    echo(term, '\x1b]1337;Capabilities\x07')
    if cursor_report_delay_ms:
        time.sleep(cursor_report_delay_ms / 1000.0)
    raw = term.flushinp(timeout=timeout)
    if not raw:
        return result

    match = re.search(r'\x1b\]1337;Capabilities=([^\x07\x1b]+)', raw)
    if not match:
        return result

    result['iterm2_features']['supported'] = True
    feature_str = match.group(1)

    FEATURE_MAP = {
        'T': ('24BIT', 'int', 2),
        'Cw': ('CLIPBOARD_WRITABLE', 'bool', 0),
        'Lr': ('DECSLRM', 'bool', 0),
        'M': ('MOUSE', 'bool', 0),
        'Sc': ('DECSCUSR', 'int', 3),
        'U': ('UNICODE_BASIC', 'bool', 0),
        'Aw': ('AMBIGUOUS_WIDE', 'bool', 0),
        'Uw': ('UNICODE_WIDTHS', 'int', 6),
        'Ts': ('TITLES', 'int', 2),
        'B': ('BRACKETED_PASTE', 'bool', 0),
        'F': ('FOCUS_REPORTING', 'bool', 0),
        'Gs': ('STRIKETHROUGH', 'bool', 0),
        'Go': ('OVERLINE', 'bool', 0),
        'Sy': ('SYNC', 'bool', 0),
        'H': ('HYPERLINKS', 'bool', 0),
        'No': ('NOTIFICATIONS', 'bool', 0),
        'Sx': ('SIXEL', 'bool', 0),
    }

    pos = 0
    while pos < len(feature_str):
        matched = False
        for code_len in (2, 1):
            code = feature_str[pos:pos + code_len]
            if code in FEATURE_MAP:
                name, ftype, bits = FEATURE_MAP[code]
                pos += code_len
                if ftype == 'int' and bits > 0:
                    digits = ''
                    while pos < len(feature_str) and feature_str[pos].isdigit():
                        digits += feature_str[pos]
                        pos += 1
                    result['iterm2_features']['features'][name] = (
                        int(digits) if digits else 0
                    )
                else:
                    result['iterm2_features']['features'][name] = True
                matched = True
                break
        if not matched:
            pos += 1

    return result


def maybe_determine_text_sizing(term, timeout=1.0):
    """Detect Kitty text sizing protocol support via CPR."""
    from ucs_detect.measure import get_location_with_retry

    result = {'text_sizing': {'width': False, 'scale': False}}

    echo(term, '\r')
    _, col0 = get_location_with_retry(term, timeout)
    if col0 == -1:
        return result

    echo(term, '\x1b]66;w=2; \x07')
    _, col1 = get_location_with_retry(term, timeout)
    if col1 == -1:
        echo(term, '\r' + ' ' * 10 + '\r')
        return result

    echo(term, '\x1b]66;s=2; \x07')
    _, col2 = get_location_with_retry(term, timeout)
    if col2 == -1:
        echo(term, '\r' + ' ' * 10 + '\r')
        return result

    if col1 - col0 == 2:
        result['text_sizing']['width'] = True
    if col2 - col1 == 2:
        result['text_sizing']['scale'] = True

    echo(term, '\r' + ' ' * max(0, col2 - col0 + 2) + '\r')
    return result


def maybe_determine_tab_stop_width(term, timeout=1.0):
    """Detect tab stop width via CPR measurement."""
    from ucs_detect.measure import get_location_with_retry

    echo(term, '\r')
    _, col0 = get_location_with_retry(term, timeout)
    if col0 == -1:
        return {}

    echo(term, '\t')
    _, col1 = get_location_with_retry(term, timeout)
    if col1 == -1:
        echo(term, '\r')
        return {}

    echo(term, '\r' + ' ' * (col1 - col0) + '\r')
    return {'tab_stop_width': col1 - col0}


def maybe_determine_kitty_notifications(term, timeout=1.0, cursor_report_delay_ms=0):
    """Detect Kitty desktop notifications (OSC 99) support."""
    echo(term, '\x1b]99;i=ucsdetect:p=?\x1b\\\x1b[c')
    if cursor_report_delay_ms:
        time.sleep(cursor_report_delay_ms / 1000.0)
    raw = term.flushinp(timeout=timeout)
    if not raw:
        return {'kitty_notifications': False}

    match = re.search(r'\x1b\]99;([^\x07\x1b]*?)[\x07\x1b]', raw)
    if match:
        params_str = match.group(1)
        result = {'kitty_notifications': {'supported': True}}
        for param in params_str.split(':'):
            if '=' in param:
                key, val = param.split('=', 1)
                if key == 'p':
                    result['kitty_notifications']['payload_types'] = val
                elif key == 'a':
                    result['kitty_notifications']['actions'] = val
        return result

    return {'kitty_notifications': False}


def maybe_determine_kitty_clipboard(term, timeout=1.0, cursor_report_delay_ms=0):
    """Detect Kitty clipboard protocol via DECRQM for mode 5522."""
    echo(term, '\x1b[?5522$p')
    if cursor_report_delay_ms:
        time.sleep(cursor_report_delay_ms / 1000.0)
    raw = term.flushinp(timeout=timeout)
    if not raw:
        return {'kitty_clipboard_protocol': False}

    match = re.search(r'\x1b\[\?5522;(\d+)\$y', raw)
    if match:
        ps = int(match.group(1))
        if ps not in (0, 4):
            return {'kitty_clipboard_protocol': True}

    return {'kitty_clipboard_protocol': False}


def maybe_determine_kitty_pointer_shapes(term, timeout=1.0, cursor_report_delay_ms=0):
    """Detect Kitty mouse pointer shapes (OSC 22) support."""
    echo(term, '\x1b]22;?__current__\x1b\\')
    if cursor_report_delay_ms:
        time.sleep(cursor_report_delay_ms / 1000.0)
    raw = term.flushinp(timeout=timeout)
    if not raw:
        return {'kitty_pointer_shapes': False}

    match = re.search(r'\x1b\]22;([^\x07\x1b]+)[\x07\x1b]', raw)
    if match:
        shape = match.group(1)
        return {'kitty_pointer_shapes': {'supported': True, 'current': shape}}

    return {'kitty_pointer_shapes': False}


def _timed_detect(func, *args, cps_tracker=None, **kwargs):
    """Call a detection function, updating cps_tracker on success.

    A result is considered successful if the returned dict contains
    any truthy values beyond default empty/False entries.
    """
    if cps_tracker is None:
        return func(*args, **kwargs)
    with cps_tracker.timing() as done_ok:
        result = func(*args, **kwargs)
        if result:
            n_items = sum(1 for v in result.values()
                          if v and v is not False)
            if n_items > 0:
                done_ok(n_items)
    return result


def do_terminal_detection(all_modes=False, cursor_report_delay_ms=0,
                          timeout=1.0, cps_tracker=None):
    writer = functools.partial(print, end="", flush=True, file=sys.stderr)
    term = make_terminal()
    attrs = {'ttype': term.kind, 'number_of_colors': term.number_of_colors}
    attrs.update(get_tty_size(term, writer))

    td = functools.partial(_timed_detect, cps_tracker=cps_tracker)

    # detect background color first so we can hide test artifacts
    with _status(writer, term, "Background Color"):
        attrs.update(td(maybe_determine_colors, term, writer))
        bg_rgb = None
        if attrs.get('background_color_rgb'):
            bg = attrs['background_color_rgb']
            bg_rgb = (bg[0] >> 8, bg[1] >> 8, bg[2] >> 8)

    attrs.update(maybe_determine_dec_modes(
        term, writer, all_modes=all_modes, bg_rgb=bg_rgb,
        timeout=timeout, cps_tracker=cps_tracker))
    with _status(writer, term, "Device Attributes", bg_rgb):
        attrs.update(td(maybe_determine_da_and_sixel, term,
                        timeout=timeout))
    with _status(writer, term, "Software Version", bg_rgb):
        attrs.update(td(maybe_determine_software, term, writer,
                        timeout=timeout))
    with _status(writer, term, "Cell Size", bg_rgb):
        attrs.update(td(maybe_determine_cell_size, term, writer,
                        timeout=timeout))
    with _status(writer, term, "Pixel Size", bg_rgb):
        attrs.update(td(maybe_determine_pixel_size, term, writer,
                        timeout=timeout))
    attrs.update(maybe_determine_screen_ratio(attrs))
    with _status(writer, term, "Kitty Keyboard", bg_rgb):
        attrs.update(td(maybe_determine_kitty_keyboard, term,
                        timeout=timeout))

    delay_kw = dict(timeout=timeout,
                    cursor_report_delay_ms=cursor_report_delay_ms)
    with term.cbreak():
        with _status(writer, term, "XTGETTCAP", bg_rgb):
            attrs.update(td(maybe_determine_xtgettcap, term,
                            **delay_kw))
        with _status(writer, term, "Kitty Graphics", bg_rgb):
            attrs.update(td(maybe_determine_kitty_graphics, term,
                            **delay_kw))
        with _status(writer, term, "iTerm2 Features", bg_rgb):
            attrs.update(td(maybe_determine_iterm2_features, term,
                            **delay_kw))
        with _status(writer, term, "Text Sizing", bg_rgb):
            attrs.update(td(maybe_determine_text_sizing, term,
                            timeout=timeout))
        with _status(writer, term, "Tab Stop Width", bg_rgb):
            attrs.update(td(maybe_determine_tab_stop_width, term,
                            timeout=timeout))
        with _status(writer, term, "Kitty Notifications", bg_rgb):
            attrs.update(td(maybe_determine_kitty_notifications,
                            term, **delay_kw))
        with _status(writer, term, "Kitty Clipboard", bg_rgb):
            attrs.update(td(maybe_determine_kitty_clipboard, term,
                            **delay_kw))
        with _status(writer, term, "Kitty Pointer Shapes", bg_rgb):
            attrs.update(td(maybe_determine_kitty_pointer_shapes,
                            term, **delay_kw))
    return attrs

if __name__ == '__main__':
    result = do_terminal_detection()
    import json
    json.dump(result, sys.stdout, indent=4, sort_keys=True)

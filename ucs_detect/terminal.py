# std imports
import os
import sys
import time
import warnings
import functools
import contextlib

# 3rd party
import blessed

SCREEN_RATIOS = [(4, 3), (16, 9), (16, 10), (21, 9), (32, 9)]


def make_terminal(fallback_kind="ansi", **kwargs):
    """
    Create a :class:`blessed.Terminal`, falling back to *fallback_kind* when ``curses.setupterm()``
    fails for the current ``$TERM``.

    The ``syncterm`` termcap is also overridden to *fallback_kind* --
    syncterm termcap has trouble with blessed+curses even when installed,
    strange cyan colors everywhere.
    """
    # syncterm termcap has trouble with blessed+curses even when installed,
    # strange cyan colors everywhere
    if os.environ.get('TERM') == 'syncterm' and 'kind' not in kwargs:
        kwargs['kind'] = fallback_kind
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        term = blessed.Terminal(**kwargs)
    if any("setupterm" in str(w.message) for w in caught):
        kwargs['kind'] = fallback_kind
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            term = blessed.Terminal(**kwargs)
    return term


@contextlib.contextmanager
def _status(writer, term, label, bg_rgb=None, silent=False):
    """Display a status line, hiding test output when bg_rgb is set."""
    if not silent:
        writer(f'\rucs-detect: {label} ..{term.clear_eol}')
    if bg_rgb is not None:
        writer(term.color_rgb(*bg_rgb))
    try:
        yield
    finally:
        if bg_rgb is not None:
            writer(term.normal)
        if not silent:
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


_DPM = blessed.Terminal.DecPrivateMode
NOTABLE_DEC_MODES = [
    _DPM.BRACKETED_PASTE,
    _DPM.SYNCHRONIZED_OUTPUT,
    _DPM.GRAPHEME_CLUSTERING,
    _DPM.IN_BAND_WINDOW_RESIZE,
    _DPM.FOCUS_IN_OUT_EVENTS,
    _DPM.MOUSE_EXTENDED_SGR,
    _DPM.BRACKETED_PASTE_MIME,
]


def maybe_determine_dec_modes(term, writer, all_modes=False, bg_rgb=None,
                              timeout=1.0, cps_tracker=None, silent=False):
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
        if not silent:
            writer(f'\rucs-detect: DEC mode {mode_num} ..{term.clear_eol}{hide}')
        t0 = time.monotonic()
        response = term.get_dec_mode(mode_num, timeout=timeout)
        elapsed = time.monotonic() - t0
        if not response.failed:
            n_ok += 1
            ok_elapsed += elapsed
            result['modes'][mode_num] = response.to_dict()
        if not silent:
            writer(unhide)
    if cps_tracker and n_ok:
        cps_tracker.update(n_ok, ok_elapsed)
    if not silent:
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
    """
    Decode DA3-style semicolon-separated ASCII values to a string.

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
        # Try ENQ (answerback) as fallback.
        if term.stream:
            term.stream.write('\x05')
            term.stream.flush()
        else:
            # Fallback to stderr if no stream
            sys.stderr.write('\x05')
            sys.stderr.flush()

        response = _read_dcs_or_plain_response(term, timeout=timeout)
        # Clean up: some terminals (e.g. SyncTERM) display ENQ as a
        # visible CP437 glyph (♣).  Overwrite it with a space.
        writer('\r' + ' ' * (term.width - 1) + '\r')
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


def maybe_determine_colors(term, writer, timeout=1.0):
    """Query terminal foreground and background colors."""
    result = {}

    r, g, b = term.get_fgcolor(timeout=timeout)
    if (r, g, b) != (-1, -1, -1):
        result['foreground_color_rgb'] = [r, g, b]
        result['foreground_color_hex'] = term.get_fgcolor_hex(timeout=timeout)

    r, g, b = term.get_bgcolor(timeout=timeout)
    if (r, g, b) != (-1, -1, -1):
        result['background_color_rgb'] = [r, g, b]
        result['background_color_hex'] = term.get_bgcolor_hex(timeout=timeout)

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


def maybe_determine_xtgettcap(term, timeout=1.0, **_kw):
    """Query terminal capabilities via XTGETTCAP (DCS+q), delegating to blessed."""
    result = {'xtgettcap': {'supported': False, 'capabilities': {}}}
    tc = term.get_xtgettcap(timeout=timeout)
    if tc is not None and tc.supported:
        result['xtgettcap']['supported'] = True
        result['xtgettcap']['capabilities'] = dict(tc.capabilities)
    return result


def maybe_determine_kitty_graphics(term, timeout=1.0, **_kw):
    """Detect Kitty graphics protocol support, delegating to blessed."""
    return {'kitty_graphics': term.does_kitty_graphics(timeout=timeout)}


def maybe_determine_iterm2_features(term, timeout=1.0, **_kw):
    """Query iTerm2 feature reporting protocol, delegating to blessed."""
    result = {'iterm2_features': {'supported': False, 'features': {}}}
    cap = term.get_iterm2_capabilities(timeout=timeout)
    if cap is not None and cap.supported:
        result['iterm2_features']['supported'] = True
        result['iterm2_features']['features'] = dict(cap.features)
    return result


def maybe_determine_text_sizing(term, timeout=1.0):
    """Detect Kitty text sizing protocol support, delegating to blessed."""
    echo(term, term.move_x(0))
    result = term.does_text_sizing(timeout=timeout)
    return {'text_sizing': {'width': result.width, 'scale': result.scale}}


def maybe_determine_tab_stop_width(term, timeout=1.0):
    """Detect tab stop width via CPR measurement."""
    # local
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


def maybe_determine_kitty_notifications(term, timeout=1.0, **_kw):
    """Detect Kitty desktop notifications (OSC 99) support, delegating to blessed."""
    if term.does_kitty_notifications(timeout=timeout):
        return {'kitty_notifications': {'supported': True}}
    return {'kitty_notifications': False}


def maybe_determine_kitty_clipboard(term, timeout=1.0, **_kw):
    """Detect Kitty clipboard protocol, delegating to blessed."""
    if term.does_kitty_clipboard(timeout=timeout):
        return {'kitty_clipboard_protocol': True}
    return {'kitty_clipboard_protocol': False}


def maybe_determine_kitty_pointer_shapes(term, timeout=1.0, **_kw):
    """Detect Kitty mouse pointer shapes (OSC 22) support, delegating to blessed."""
    shape = term.does_kitty_pointer_shapes(timeout=timeout)
    if shape is not None:
        return {'kitty_pointer_shapes': {'supported': True, 'current': shape}}
    return {'kitty_pointer_shapes': False}


def _timed_detect(func, *args, cps_tracker=None, **kwargs):
    """
    Call a detection function, updating cps_tracker on success.

    A result is considered successful if the returned dict contains any truthy values beyond default
    empty/False entries.
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
                          timeout=1.0, cps_tracker=None, has_unicode=True,
                          silent=False):
    writer = functools.partial(print, end="", flush=True, file=sys.stderr)
    term = make_terminal()
    attrs = {'ttype': term.kind, 'number_of_colors': term.number_of_colors}
    attrs.update(get_tty_size(term, writer))

    td = functools.partial(_timed_detect, cps_tracker=cps_tracker)

    # detect background color first so we can hide test artifacts
    with _status(writer, term, "Background Color", silent=silent):
        attrs.update(td(maybe_determine_colors, term, writer,
                        timeout=timeout))
        bg_rgb = None
        if attrs.get('background_color_rgb'):
            bg = attrs['background_color_rgb']
            bg_rgb = (bg[0] >> 8, bg[1] >> 8, bg[2] >> 8)

    # probe for "modern" terminal: DA1 and XTVERSION are cheap queries that
    # modern terminals respond to and retro terminals (linux fbdev, real
    # VT100, etc.) ignore.  kitty responds to XTVERSION but not DA1.
    with _status(writer, term, "Device Attributes", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_da_and_sixel, term,
                        timeout=timeout))
    with _status(writer, term, "Software Version", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_software, term, writer,
                        timeout=timeout))

    with _status(writer, term, "Cell Size", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_cell_size, term, writer,
                        timeout=timeout))
    with _status(writer, term, "Pixel Size", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_pixel_size, term, writer,
                        timeout=timeout))
    attrs.update(maybe_determine_screen_ratio(attrs))

    has_device_attrs = attrs.get('device_attributes') is not None
    has_sw_version = attrs.get('software_name') is not None
    has_cell_size = attrs.get('cell_height') is not None
    is_modern = has_unicode and (has_device_attrs or has_sw_version
                                 or has_cell_size)

    if not is_modern:
        return attrs

    attrs.update(maybe_determine_dec_modes(
        term, writer, all_modes=all_modes, bg_rgb=bg_rgb,
        timeout=timeout, cps_tracker=cps_tracker, silent=silent))

    with _status(writer, term, "Kitty Keyboard", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_kitty_keyboard, term,
                        timeout=timeout))

    with _status(writer, term, "XTGETTCAP", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_xtgettcap, term,
                        timeout=timeout))
    with _status(writer, term, "Kitty Graphics", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_kitty_graphics, term,
                        timeout=timeout))
    with _status(writer, term, "iTerm2 Features", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_iterm2_features, term,
                        timeout=timeout))
    with _status(writer, term, "Text Sizing", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_text_sizing, term,
                        timeout=timeout))
    with _status(writer, term, "Tab Stop Width", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_tab_stop_width, term,
                        timeout=timeout))
    with _status(writer, term, "Kitty Notifications", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_kitty_notifications, term,
                        timeout=timeout))
    with _status(writer, term, "Kitty Clipboard", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_kitty_clipboard, term,
                        timeout=timeout))
    with _status(writer, term, "Kitty Pointer Shapes", bg_rgb, silent=silent):
        attrs.update(td(maybe_determine_kitty_pointer_shapes, term,
                        timeout=timeout))
    return attrs


if __name__ == '__main__':
    result = do_terminal_detection()
    # std imports
    import json
    json.dump(result, sys.stdout, indent=4, sort_keys=True)

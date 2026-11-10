"""Measure the horizontal cursor advance of control characters."""

from __future__ import annotations

# std imports
import os
import collections

# local
from ucs_detect import terminal as terminal_mod
from ucs_detect.measure import get_location_with_retry

Probe = collections.namedtuple('Probe', ('codepoint', 'encoding', 'data'))

#: Controls with no standard cursor motion, charset shift, or parser state change.
_C0 = (0x00, 0x01, 0x02, 0x03, 0x04, 0x06, 0x10, 0x12, 0x14, 0x15,
       0x16, 0x17, 0x19, 0x1C, 0x1D, 0x1E, 0x1F, 0x7F)
_C1 = (0x80, 0x81, 0x82, 0x83, 0x86, 0x87, 0x91, 0x92, 0x93, 0x94,
       0x95, 0x96, 0x97, 0x99)
_CLEANUP = b'\x18\x1b\\\x0f'


def iter_probes():
    """Yield every control character probe in a stable order."""
    for codepoint in _C0:
        yield Probe(codepoint, 'raw', bytes([codepoint]))
    for codepoint in _C1:
        yield Probe(codepoint, 'utf-8', chr(codepoint).encode('utf-8'))


def _write_bytes(term, data):
    """Write *data* to the terminal without the text stream encoding it again."""
    stream = term.stream
    stream.flush()
    try:
        os.write(stream.fileno(), data)
    except (AttributeError, OSError):
        buffer = getattr(stream, 'buffer', None)
        if buffer is not None:
            buffer.write(data)
            buffer.flush()
        else:
            stream.write(data.decode('latin1'))
            stream.flush()


def _park_row(term):
    """Return a row away from both scroll margins."""
    return min(max(1, term.height // 2), max(1, term.height - 2))


def _park_column(term):
    """Return a column with room on both sides."""
    return min(10, max(1, term.width - 2))


def _probe_one(term, park_y, park_x, probe, timeout):
    """Return the horizontal cursor advance of one control character."""
    terminal_mod.echo(term, term.move_yx(park_y, park_x) + term.clear_eol)
    y0, x0 = get_location_with_retry(term, timeout)
    if (y0, x0) == (-1, -1):
        return None

    _write_bytes(term, probe.data)
    _write_bytes(term, _CLEANUP)
    term.flushinp(timeout=0.02)

    y1, x1 = get_location_with_retry(term, timeout)
    if (y1, x1) == (-1, -1):
        return None
    return x1 - x0


def maybe_determine_control_advance(term, timeout=1.0, **_kwargs):
    """
    Measure the horizontal cursor advance of selected C0, DEL, and C1 controls.

    Each probe parks the cursor mid-screen, records its column, writes one control character, resets
    the parser with CAN, ST, and SI, and records the new column.  C1 characters are probed in their
    UTF-8 encoding, which reaches the parser as U+0080 through U+009F.

    :returns: dict with a ``control_advance`` mapping of ``U+XXXX/encoding`` to column delta.
    """
    if not term.is_a_tty or term.height < 3 or term.width < 3:
        return {}
    advance = {}
    park_y = _park_row(term)
    park_x = _park_column(term)
    original_y, original_x = get_location_with_retry(term, timeout)
    try:
        # Raw mode disables line-discipline output processing, so the terminal
        # sees the control byte unchanged.
        with term.raw():
            for probe in iter_probes():
                dx = _probe_one(term, park_y, park_x, probe, timeout)
                if dx is not None:
                    key = f'U+{probe.codepoint:04X}/{probe.encoding}'
                    advance[key] = dx
    finally:
        terminal_mod.echo(term, term.clear_eol)
        if (original_y, original_x) != (-1, -1):
            terminal_mod.echo(term, term.move_yx(original_y, original_x))
    return {'control_advance': advance}

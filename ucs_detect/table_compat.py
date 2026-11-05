"""Compatibility helpers for older prettytable releases."""
# 3rd party
import wcwidth
import prettytable


def _detect_alignment_dict():
    table = prettytable.PrettyTable()
    table.field_names = ["A", "B"]
    try:
        table.align = {"A": "l", "B": "r"}
    except Exception:  # pylint: disable=broad-except
        return False
    return True


def _detect_ansi_width():
    widths = []
    try:
        for cell in ("X", "\x1b[31mX\x1b[0m"):
            table = prettytable.PrettyTable()
            table.field_names = ["A"]
            table.add_row([cell])
            widths.append(len(str(table).splitlines()[0]))
    except Exception:  # pylint: disable=broad-except
        return False
    return widths[0] == widths[1]


SUPPORTS_ALIGNMENT_DICT = _detect_alignment_dict()
SUPPORTS_ANSI_WIDTH = _detect_ansi_width()


def _clean(value):
    if SUPPORTS_ANSI_WIDTH or not isinstance(value, str):
        return value
    return wcwidth.strip_sequences(value)


def new_table(title=None, field_names=None, align=None):
    """Return a PrettyTable, degrading gracefully on older releases."""
    table = prettytable.PrettyTable()
    if title is not None:
        table.title = _clean(title)
    if field_names is not None:
        table.field_names = [_clean(name) for name in field_names]
    if align is not None and SUPPORTS_ALIGNMENT_DICT:
        table.align = align
    return table


def add_row(table, values):
    """Add a row, removing SGR when prettytable cannot measure it."""
    table.add_row([_clean(value) for value in values])

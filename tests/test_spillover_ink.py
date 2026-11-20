"""Tests for the spillover scan's ink check."""

from PIL import Image, ImageDraw

from ucs_detect import spillover

CELL_W = 10
CELL_H = 20
BAR_A = (40, 40, 160)
BAR_B = (160, 40, 40)
BACKGROUND = (0, 0, 0)
INK = (255, 255, 255)


def _page(column, advance):
    """Return a one-row page of bars with an *advance* cell glyph background at *column*."""
    calibration = spillover.Calibration(0, 0, CELL_W, CELL_H, 8, 1)
    image = Image.new('RGB', (8 * CELL_W, CELL_H))
    draw = ImageDraw.Draw(image)
    for cell in range(8):
        draw.rectangle((cell * CELL_W, 0, (cell + 1) * CELL_W - 1, CELL_H - 1),
                       fill=BAR_A if cell % 2 else BAR_B)
    draw.rectangle((column * CELL_W, 0, (column + advance) * CELL_W - 1, CELL_H - 1),
                   fill=BACKGROUND)
    return image, draw, calibration


def test_empty_grapheme_is_blank():
    image, _draw, calibration = _page(2, 2)
    assert not spillover.cell_is_painted(image, calibration, 0, 2, 2)


def test_stroke_centred_in_wide_grapheme_is_ink():
    # A '1' centred in a two cell emoji tile: a 2px stem on the boundary between the cells.
    image, draw, calibration = _page(2, 2)
    stem_x = 3 * CELL_W - 1
    draw.rectangle((stem_x, 4, stem_x + 1, 15), fill=INK)
    assert spillover.cell_is_painted(image, calibration, 0, 2, 2)


def test_mark_below_the_baseline_is_ink():
    # A dot below (U+0323) on a space: ink only in the bottom fifth of the cell.
    image, draw, calibration = _page(2, 1)
    draw.rectangle((24, 16, 25, 17), fill=INK)
    assert spillover.cell_is_painted(image, calibration, 0, 2, 1)


def test_small_mark_is_not_diluted_by_the_whole_cell():
    # A Tibetan vowel sign on a space: a few pixels, which the inner box alone calls ink.
    image, draw, calibration = _page(2, 1)
    draw.rectangle((24, 8, 25, 8), fill=INK)
    assert spillover.cell_is_painted(image, calibration, 0, 2, 1)


def test_neighbouring_bars_are_not_ink():
    # Calibration a pixel off: the bars of the cells beside the grapheme must not count.
    image, _draw, calibration = _page(2, 1)
    calibration = calibration._replace(origin_x=1)
    assert not spillover.cell_is_painted(image, calibration, 0, 2, 1)

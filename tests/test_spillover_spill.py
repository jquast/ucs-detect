"""Tests for the spillover scan's neighbour (spill) check."""

import collections

from PIL import Image, ImageDraw

from ucs_detect import spillover

CELL_W = 10
CELL_H = 20
CELLS = 8
COLUMN = spillover.LEFT_CELLS
BAR_A = (40, 40, 160)
BAR_B = (160, 40, 40)
BACKGROUND = (16, 16, 16)
INK = (255, 255, 255)

Candidate = collections.namedtuple('Candidate', 'advance width')


def _bar(cell):
    return BAR_A if cell % 2 else BAR_B


def _page():
    """Return a one-row page of bars with a one cell grapheme background at COLUMN."""
    calibration = spillover.Calibration(0, 0, CELL_W, CELL_H, CELLS, 1)
    image = Image.new('RGB', (CELLS * CELL_W, CELL_H))
    draw = ImageDraw.Draw(image)
    for cell in range(CELLS):
        draw.rectangle((cell * CELL_W, 0, (cell + 1) * CELL_W - 1, CELL_H - 1),
                       fill=_bar(cell))
    draw.rectangle((COLUMN * CELL_W, 0, (COLUMN + 1) * CELL_W - 1, CELL_H - 1),
                   fill=BACKGROUND)
    return image, draw, calibration


def _spill(image, calibration):
    reference = [_bar(cell) for cell in range(CELLS)]
    items = [(0, COLUMN, Candidate(1, 1))]
    result, = spillover.analyze_page(image, calibration, items, reference=reference)
    return result['left_cells'], result['right_cells']


def test_clean_grapheme_does_not_spill():
    image, draw, calibration = _page()
    draw.rectangle((COLUMN * CELL_W + 3, 5, COLUMN * CELL_W + 6, 14), fill=INK)
    assert _spill(image, calibration) == (0, 0)


def test_mark_low_in_the_next_cell_is_spill():
    # Arabic tanween drawn a cell right of its letter: a dot in the bottom fifth of the next cell.
    image, draw, calibration = _page()
    x = (COLUMN + 1) * CELL_W + 4
    draw.rectangle((x, 16, x + 2, 18), fill=INK)
    assert _spill(image, calibration) == (0, 1)


def test_overhang_into_the_edge_of_the_cell_before_is_spill():
    # A glyph reaching 3px into the cell before it, outside that cell's middle 60%.
    image, draw, calibration = _page()
    x1 = COLUMN * CELL_W - 1
    draw.rectangle((x1 - 2, 6, x1, 13), fill=INK)
    assert _spill(image, calibration) == (1, 0)


def test_a_stray_pixel_is_not_spill():
    # One antialiasing pixel past the cell edge is below the threshold the ink check uses.
    image, draw, calibration = _page()
    draw.point(((COLUMN + 1) * CELL_W + 2, 10), fill=INK)
    assert _spill(image, calibration) == (0, 0)


def test_calibration_a_pixel_off_is_not_spill():
    # The grapheme's own background, one pixel into a neighbour's box, is not spill.
    image, _draw, calibration = _page()
    calibration = calibration._replace(origin_x=1)
    assert _spill(image, calibration) == (0, 0)
    calibration = calibration._replace(origin_x=-1)
    assert _spill(image, calibration) == (0, 0)

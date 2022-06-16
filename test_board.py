import pytest

from board import Board


def test_board_init():
    size = 3
    board = Board(size)

    assert size == board.size
    assert size == len(board.cells)
    assert size == len(board.cells[0])

    # test labels are correct
    assert ["1", "2", "3"] == board.row_labels[0]
    assert ["4", "5", "6"] == board.row_labels[1]
    assert ["7", "8", "9"] == board.row_labels[2]
    assert ["1", "4", "7"] == board.col_labels[0]
    assert ["2", "5", "8"] == board.col_labels[1]
    assert ["3", "6", "9"] == board.col_labels[2]
    assert ["1", "5", "9"] == board.diag_labels[0]
    assert ["3", "5", "7"] == board.diag_labels[1]


def test_label_to_cell_mapping():
    board = Board(3)
    # test updating cell directly and then getting it's contents by label
    assert " " == board.get_cell_contents("5")
    board.cells[1][1] = "X"
    assert "X" == board.get_cell_contents("5")


def test_cell_labels_are_correct():
    board = Board(3)

    # test label maps to correct cells
    assert "1" == board.get_cell_label(0, 0)
    assert "3" == board.get_cell_label(0, 2)
    assert "5" == board.get_cell_label(1, 1)
    assert "7" == board.get_cell_label(2, 0)
    assert "9" == board.get_cell_label(2, 2)


def test_available_cells():
    board = Board(3)

    available_cells = board.get_available_cell_labels()
    assert 9 == len(available_cells)

    board.cells[1][1] = "X"
    available_cells = board.get_available_cell_labels()
    assert 8 == len(available_cells)
    assert "5" not in available_cells


def test_set_cell_contents():
    board = Board(3)

    board.set_cell_contents("5", "X")
    assert "X" == board.get_cell_contents("5")


def test_is_winner():
    board = Board(3)
    mark = "X"

    # lets fast forward to some winning scenarios
    # rows
    board.set_cell_contents("1", mark)
    board.set_cell_contents("2", mark)
    board.set_cell_contents("3", mark)
    assert board.is_winner(mark)

    board.reset_to_empty()
    board.set_cell_contents("4", mark)
    board.set_cell_contents("5", mark)
    board.set_cell_contents("6", mark)
    assert board.is_winner(mark)

    board.reset_to_empty()
    board.set_cell_contents("7", mark)
    board.set_cell_contents("8", mark)
    board.set_cell_contents("9", mark)
    assert board.is_winner(mark)

    # cols
    board.reset_to_empty()
    board.set_cell_contents("1", mark)
    board.set_cell_contents("4", mark)
    board.set_cell_contents("7", mark)
    assert board.is_winner(mark)

    board.reset_to_empty()
    board.set_cell_contents("2", mark)
    board.set_cell_contents("5", mark)
    board.set_cell_contents("8", mark)
    assert board.is_winner(mark)

    board.reset_to_empty()
    board.set_cell_contents("3", mark)
    board.set_cell_contents("6", mark)
    board.set_cell_contents("9", mark)
    assert board.is_winner(mark)

    # diag
    board.reset_to_empty()
    board.set_cell_contents("1", mark)
    board.set_cell_contents("5", mark)
    board.set_cell_contents("9", mark)
    assert board.is_winner(mark)

    board.reset_to_empty()
    board.set_cell_contents("3", mark)
    board.set_cell_contents("5", mark)
    board.set_cell_contents("7", mark)
    assert board.is_winner(mark)

import pytest
from board import Board
from player import Player

def test_board_setup():
    board = Board(3)

    assert 9 == board.count_available_cells()
    expect_available = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    available = board.available_cells()
    for label in expect_available:
        assert label in available


def test_first_move():
    player1 = Player("Dave", "X")

    board = Board(3)

    move_choice = "5"
    board.make_move(player1, move_choice)

    assert 8 == board.count_available_cells()
    assert move_choice not in board.available_cells()











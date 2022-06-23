import pytest

from board import Board
from game import Game
from player import Player


def test_turn():
    board = Board(3)
    player1 = Player("Dave", "X")
    player2 = Player("Alison", "O")
    game = Game(board, player1, player2)

    assert True == game.turn(player1, "5")  # valid turn
    assert False == game.turn(player2, "5")  # invalid turn since label "5" not empty


def test_is_game_over():
    board = Board(3)

    # lets fast forward to some winning scenarios
    board.set_cell_contents("1", "X")
    board.set_cell_contents("2", "X")
    board.set_cell_contents("3", "X")
    game = Game(board, Player("Dave", "X"), Player("Alison", "O"))
    assert game.is_game_over()


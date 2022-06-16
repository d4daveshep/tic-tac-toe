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

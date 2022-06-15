import Game as Game
import pytest
from board import Board
from player import Player
from game import Game

def test_run_game():
    board = Board(3)
    player1 = Player("Dave", "X")
    player2 = Player("Alison", "O")

    game = Game(board, player1, player2)
    assert not game.is_game_over()

    game.turn(player1, "5")
    assert not game.is_game_over()







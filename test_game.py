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
    mark_X = "X"
    mark_O = "O"

    player_1 = Player("Dave", mark_X)
    player_2 = Player("Alison", mark_O)
    game = Game(board, player_1, player_2)

    # lets fast forward to some winning scenarios
    board.set_cell_contents("1", mark_X)
    board.set_cell_contents("2", mark_X)
    board.set_cell_contents("3", mark_X)

    assert game.is_game_over()
    assert game.get_winner() == player_1


    board.reset_to_empty()
    # lets fast forward to some winning scenarios
    board.set_cell_contents("1", mark_O)
    board.set_cell_contents("2", mark_O)
    board.set_cell_contents("3", mark_O)
    assert game.is_game_over()
    assert game.get_winner() == player_2


def test_is_game_draw():
    board = Board(3)
    mark_X = "X"
    mark_O = "O"

    player_1 = Player("Dave", mark_X)
    player_2 = Player("Alison", mark_O)
    game = Game(board, player_1, player_2)
    assert not game.is_game_draw()

    moves = list("13246578")  # do 8 moves only
    # XX0
    # OOX
    # XOX

    while moves:
        move = moves.pop(0)
        game.turn(player_1, move)
        board.display_board()
        assert not game.is_game_over()

        move = moves.pop(0)
        game.turn(player_2, move)
        board.display_board()
        assert not game.is_game_over()

    game.turn(player_1,"9")  # play last cell, game is now over and is a draw
    assert game.is_game_over()
    assert game.is_game_draw()

    assert game.get_winner() is None

    # board.display_board()

def test_run_game_player_wins():
    board = Board(3)
    mark_X = "X"
    mark_O = "O"

    player_1 = Player("Dave", mark_X)
    player_2 = Player("Alison", mark_O)
    game = Game(board, player_1, player_2)

    assert not game.is_game_over()

    # alternate moves into square 1, 2, 3, etc.  At move 7 player1 wins on daig[1]
    # XOX
    # OXO
    # X
    moves = list("123456")  # do first 6 moves only

    while moves:
        move = moves.pop(0)
        game.turn(player_1, move)
        board.display_board()
        assert not game.is_game_over()

        move = moves.pop(0)
        game.turn(player_2, move)
        board.display_board()
        assert not game.is_game_over()

    game.turn(player_1,"7")  # player_1 now wins and game is over
    assert game.is_game_over()
    assert game.get_winner() is player_1

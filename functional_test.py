import pytest
from board import Board
from player import Player
from game import Game


def test_run_game_player_wins():
    board = Board(3)
    player1 = Player("Dave", "X")
    player2 = Player("Alison", "O")

    game = Game(board, player1, player2)
    assert not game.is_game_over()

    # alternate moves into square 1, 2, 3, etc.  At move 7 player1 wins on daig[1]
    move = 0
    while True:
        move += 1
        assert game.turn(player1, str(move))
        if move == 7:
            assert game.is_game_over()
            break
        else:
            assert not game.is_game_over()
        move += 1
        assert game.turn(player2, str(move))
        assert not game.is_game_over()
    else:
        assert False  # fail if we get to here

def test_game_is_draw():
    board = Board(3)
    player1 = Player("Dave", "X")
    player2 = Player("Alison", "O")

    game = Game(board, player1, player2)
    #
    # XX0
    # OOX
    # XOX
    moves = list("132465789")
    #
    print()
    # board.display_board()
    while True:
        move = moves.pop(0)
        game.turn(player1, move)
        board.display_board()
        if game.is_game_over():
            break
        move = moves.pop(0)
        game.turn(player2, move)
        board.display_board()
        if game.is_game_over():
            break
    else:
        assert False

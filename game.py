import pytest


class Game:

    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def is_game_over(self):
        return False

import pytest
from player import Player


class Game:

    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def is_game_over(self):
        return False

    def turn(self, player1, cell_label):
        valid_labels = self.board.get_available_cell_labels()
        if cell_label in valid_labels:
            self.board.set_cell_contents(cell_label, player1.mark)
            return True
        else:
            return False



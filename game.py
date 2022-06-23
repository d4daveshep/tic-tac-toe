import pytest

from board import Board
from player import Player


class Game:

    def __init__(self, board: Board, player1: Player, player2: Player):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def is_game_over(self) -> bool:
        return self.board.is_winner("X")

    def turn(self, player1: Player, cell_label: str) -> bool:
        valid_labels = self.board.get_available_cell_labels()
        if cell_label in valid_labels:
            self.board.set_cell_contents(cell_label, player1.mark)
            return True
        else:
            return False

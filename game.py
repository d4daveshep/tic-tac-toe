import pytest

from board import Board
from player import Player


class Game:

    def __init__(self, board: Board, player1: Player, player2: Player):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def is_game_over(self) -> bool:
        """
        The game is over when either player has won or the board is full and neither player has won i.e.  game is drawn
        :return:
        """
        return (self.board.is_full() or \
               self.board.is_winner(self.player1.mark) or \
               self.board.is_winner(self.player2.mark) )

    def get_winner(self) -> Player:
        if self.board.is_winner(self.player1.mark):
            return self.player1
        elif self.board.is_winner(self.player2.mark):
            return self.player2
        else:
            return None


    def is_game_draw(self) -> bool:
        """
        Game is a draw if all cells are filled and there is no winner
        :return:
        """
        return self.board.is_full() #and self.get_winner() is None


    def turn(self, player1: Player, cell_label: str) -> bool:
        valid_labels = self.board.get_available_cell_labels()
        if cell_label in valid_labels:
            self.board.set_cell_contents(cell_label, player1.mark)
            return True
        else:
            return False

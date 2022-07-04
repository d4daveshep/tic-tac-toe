# play a game of tic tac toe against computer
import random

from board import Board
from game import Game
from player import Player

print("*** starting game ***")
player_name = ""
while not player_name.isalpha():
    player_name = input("Enter your name...")
player_name = player_name.title()

player_mark = ""
while player_mark != "X" and player_mark != "O":
    player_mark = input("Enter your mark X or O...")

player_1_or_2 = 0
while player_1_or_2 < 1 or player_1_or_2 > 2:
    try:
        player_1_or_2 = int(input("Do you want to go first(1) or second(2)..."))
    except ValueError:
        pass

print(f"OK {player_name}, you're using {player_mark} and you are player {player_1_or_2}")

computer_mark = ""
if player_mark == "X":
    computer_mark = "O"
else:
    computer_mark = "X"

computer_number = 0
if player_1_or_2 == 1:
    computer_number = 2
else:
    computer_number = 1

print(f"Computer will use {computer_mark} and is player {computer_number}")

player = Player(player_name, player_mark)
computer = Player("Computer", computer_mark)

board = Board(3)
game = Game(board, player, computer)

whose_turn = None
if player_1_or_2 == 1:
    whose_turn = player
else:
    whose_turn = computer

input("Press Enter to continue...")

board.display_board()

while not game.is_game_over():
    available_cells = board.get_available_cell_labels()

    if whose_turn == player:
        available_cells = board.get_available_cell_labels()
        cell_chosen = ""
        while not (cell_chosen.isdigit() and cell_chosen in available_cells):
            cell_chosen = input("Enter the number to place your mark")
        game.turn(whose_turn, cell_chosen)
        if game.is_game_over():
            break
        whose_turn = computer

    if whose_turn == computer:
        cell_chosen = random.choice(available_cells)
        game.turn(whose_turn, cell_chosen)
        print(f"Computer chose {cell_chosen}")
        if game.is_game_over():
            break
        whose_turn = player

    board.display_board()

board.display_board()
if game.is_game_draw():
    print("Game over and it's a DRAW")
else:
    winner_name = game.get_winner().name
    print(f"Winner is {winner_name}")

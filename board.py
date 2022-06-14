
class Board:

    def __init__(self, size=3):
        self.board_size = size
        self.cells = [[str((i + 1) + (j * 3)) for i in range(self.board_size)] for j in
                 range(self.board_size)]  # 2D list comprehension

    def count_available_cells(self):
        return self.board_size * self.board_size

    def available_cells(self):
        cell_list = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                cell_list.append(self.cells[i][j])
        return cell_list

    def make_move(self, player, cell_label):
        None

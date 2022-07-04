class Board:
    """
    Implements a square board, implemented by a 2-D array of cells that contain a string either a space, X or O.
    Each cell has a label, which is a digit string. E.g. "1" to "9" for a 3 x 3 grid starting from top left and
    increasing row by row.

    Methods are provided to map between cell labels and cell contents and row, column indexes.

    Internally, the board also has list of row, column and diagonal labels to help with checking if a player has won
    the game.

    """

    def __init__(self, size: int = 3):

        assert size > 1
        self.size = size

        #  create the cell grid and fill with space character
        self.reset_to_empty()

        # create the dict for cell_labels
        self.cell_labels = {}

        # create the lists of row, col and diag labels
        self.row_labels = []
        self.col_labels = []
        self.diag_labels = [[], []]  # diag[0] is \,  diag[1] is /

        # build the containers for row and col labels
        for i in range(self.size):
            self.row_labels.append(i)
            self.row_labels[i] = []
            self.col_labels.append(i)
            self.col_labels[i] = []

        for i in range(self.size):
            for j in range(self.size):
                label = self.get_cell_label(i, j)
                self.cell_labels[label] = (i, j)
                self.row_labels[i].append(label)
                self.col_labels[j].append(label)

                if i == j:
                    self.diag_labels[0].append(label)
                if i == (self.size - 1 - j):
                    self.diag_labels[1].append(label)

    def reset_to_empty(self):
        #  create the 2D cell grid using list comprehension to fill with space character
        self.cells = [[" " for i in range(self.size)] for j in range(self.size)]

    def get_cell_label(self, row: int, col: int) -> str:  # row, col are zero-based
        return str((row * self.size) + (col + 1))

    def get_cell_contents(self, label: str) -> str:
        row = self.cell_labels[label][0]
        col = self.cell_labels[label][1]
        return self.cells[row][col]

    def set_cell_contents(self, label: str, mark: str):
        row = self.cell_labels[label][0]
        col = self.cell_labels[label][1]
        self.cells[row][col] = mark

    # def count_available_cells(self):
    #     return self.size * self.size

    def get_available_cell_labels(self) -> list:
        cell_list = []
        for row_num, row in enumerate(self.cells):
            for col_num, cell in enumerate(row):
                if cell == " ":
                    cell_list.append(self.get_cell_label(row_num, col_num))
        return cell_list

    def is_winner(self, mark: str) -> bool:
        all_lines = self.row_labels + self.col_labels + self.diag_labels
        for line in all_lines:
            if self.check_row_col_diag_have_same_mark(line, mark):
                return True
        return False

    def check_row_col_diag_have_same_mark(self, line, mark):
        for label in line:
            if self.get_cell_contents(label) != mark:
                return False
        return True

    def count_available_cells(self):
        return len(self.get_available_cell_labels())

    def display_board(self):
        # The function prints the board's current status to the console
        print()
        draw_divider = "+-------+-------+-------+"
        draw_spacer = "|       |       |       |"
        for i in range(self.size):
            print(draw_divider)
            print(draw_spacer)
            for j in range(self.size):
                if self.cells[i][j] == " ":
                    print("|   ", self.get_cell_label(i,j), "   ", sep="", end="")
                else:
                    print("|   ", self.cells[i][j], "   ", sep="", end="")
            print("|")
            print(draw_spacer)
        print(draw_divider)

    def is_full(self):
        if self.count_available_cells() > 0:
            return False
        else:
            return True

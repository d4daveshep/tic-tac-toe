class Board:

    def __init__(self, size=3):
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


    def get_cell_label(self, row, col):  # row, col are zero-based
        return str((row * self.size) + (col + 1))

    def get_cell_contents(self, label):
        row = self.cell_labels[label][0]
        col = self.cell_labels[label][1]
        return self.cells[row][col]

    def set_cell_contents(self, label, mark):
        row = self.cell_labels[label][0]
        col = self.cell_labels[label][1]
        self.cells[row][col] = mark

    # def count_available_cells(self):
    #     return self.size * self.size

    def get_available_cell_labels(self):
        cell_list = []
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j] == " ":
                    cell_list.append(self.get_cell_label(i, j))
        return cell_list

    def is_winner(self, mark):
        for row in self.row_labels:
            if self.check_row_col_diag_have_same_mark(row, mark):
                return True
        for col in self.col_labels:
            if self.check_row_col_diag_have_same_mark(col, mark):
                return True
        for diag in self.diag_labels:
            if self.check_row_col_diag_have_same_mark(diag, mark):
                return True
        return False

    def check_row_col_diag_have_same_mark(self, line, mark):
        for label in line:
            if self.get_cell_contents(label) != mark:
                return False
        return True

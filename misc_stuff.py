def get_available_cell_labels(cells: list) -> list:
    cell_list = []
    for row_num, row in enumerate(cells):
        for col_num, cell in enumerate(row):
            if cell == " ":
                cell_list.append(row_num * 3 + col_num)
    return cell_list


# set up the 2D grid of cells using list comprehension
size = 3
# cells = [[1+(row*size + col) for col in range(size)] for row in range(size)] # calculate cell labels
# cells = [[(row,col) for col in range(size)] for row in range(size)] # fill cells with row,col tuple
cells = [[" " for col in range(size)] for row in range(size)]

for row in cells:
    for cell in row:
        print(cell, end=" ")
    print()

print()
print(f"available cell labels are... {get_available_cell_labels(cells)}")
# print(cells[0])

from typing import Iterator


def get_row_labels_iter(row_num: int) -> Iterator[str]:
    row_labels_iter = (str((row_num * size + col + 1)) for col in range(size))
    return row_labels_iter


def get_col_labels_iter(col_num: int) -> Iterator[str]:
    col_labels_iter = (str(row_num * size + col_num + 1) for row_num in range(size))
    return col_labels_iter


def get_positive_diag_labels_iter() -> Iterator[str]:
    labels_iter = (str(row_num * size + row_num + 1) for row_num in range(size))
    return labels_iter


def get_negative_diag_labels_iter() -> Iterator[str]:
    # if i == (self.size - 1 - j):
    #     self.diag_labels[1].append(label)

    labels_iter = (str((row_num + 1) * size - row_num) for row_num in range(size))
    return labels_iter


# size = 5
labels = get_row_labels_iter(0)
print(list(labels))
labels = get_row_labels_iter(1)
print(list(labels))
labels = get_row_labels_iter(2)
print(list(labels))
print()

labels = get_col_labels_iter(0)
print(list(labels))
labels = get_col_labels_iter(1)
print(list(labels))
labels = get_col_labels_iter(2)
print(list(labels))
print()

labels = get_positive_diag_labels_iter()
print(list(labels))
labels = get_negative_diag_labels_iter()
print(list(labels))

def get_available_cell_labels(cells: list) -> list:
    cell_list = []
    for row_num, row in enumerate(cells):
        for col_num, cell in enumerate(row):
            if cell == " ":
                cell_list.append(row_num*3 + col_num)
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

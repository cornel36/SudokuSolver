# 1 define the sudoku grid
grid = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]

# 2 find an empty cell


def find_blank(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                return row, col
    return None


# 3 check if number exists in given column


def check_col(grid, column, number):
    for row in range(len(grid)):
        if grid[row][column] == number:
            return True
    return False


# 4 check if number exists in given row


def check_row(grid, row, number):
    for col in range(len(grid[0])):
        if grid[row][col] == number:
            return True
    return False


# 5 check if number exists in a subgrid


def check_3x3(grid, start_row, start_col, number):
    for row in range(3):
        for col in range(3):
            if grid[row + start_row][col + start_col] == number:
                return True
    return False


# 6 check if number can be put in selected spot


def is_valid(grid, row, col, number):
    return (
        not check_row(grid, row, number)
        and not check_col(grid, col, number)
        and not check_3x3(grid, row - row % 3, col - col % 3, number)
    )


# 7 combine all


def solve_sudoku(grid):
    empty_cell = find_blank(grid)
    if empty_cell is None:
        return True

    row, col = empty_cell

    for number in range(1, 10):
        if is_valid(grid, row, col, number):
            grid[row][col] = number

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False


# 8 SOLVE !!!!!

if solve_sudoku(grid):
    print("Solution:")
    for row in grid:
        print(row)
else:
    print("There's no solution")

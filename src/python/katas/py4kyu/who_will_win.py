"""Kata url: https://www.codewars.com/kata/56882731514ec3ec3d000009."""

POS = {k: c for c, k in enumerate("ABCDEFG")}
YES = ((1, (1, 0)), (2, (0, 1)), (4, (1, 1)), (8,  (1, -1)))
CHECKS = [
    [0x7, 0x7, 0x7, 0x2, 0x2, 0x2],
    [0x7, 0x7, 0x7, 0x2, 0x2, 0x2],
    [0x7, 0x7, 0x7, 0x2, 0x2, 0x2],
    [0xf, 0xf, 0xf, 0x2, 0x2, 0x2],
    [0x9, 0x9, 0x9, 0x0, 0x0, 0x0],
    [0x9, 0x9, 0x9, 0x0, 0x0, 0x0],
    [0x9, 0x9, 0x9, 0x0, 0x0, 0x0]
]


def check_cell(board, x, y, d):
    dx, dy = d
    return board[y][x] * all(
        board[y][x] == board[y + (dy * n)][x + (dx * n)]
        for n in range(4)
    )


def check_cell_win(board, x, y):
    cell_check = CHECKS[y][x]
    if not cell_check:
        return

    w = 0
    for c, cd in YES:
        if cell_check & c:
            w |= check_cell(board, x, y, cd)
    return w


def check_board_win(board):
    for y, line in enumerate(board):
        for x, cell in enumerate(line):
            if cell == 0:
                continue

            if w := check_cell_win(board, x, y):
                return w


def who_is_winner(pieces_position_list):
    grid = [[0 for _ in range(6)] for _ in range(7)]

    for piece in pieces_position_list:
        pos, color = piece.split('_')

        i = grid[p := POS[pos]].index(0)
        grid[p][i] = 1 + (color[0] == 'Y')

        if w := check_board_win(grid):
            return ("Red", "Yellow", "Draw")[w - 1]
    return "Draw"

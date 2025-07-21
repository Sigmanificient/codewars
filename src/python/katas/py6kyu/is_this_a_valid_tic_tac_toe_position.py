"""Kata url: https://www.codewars.com/kata/68582183cf16719a5ba943df."""
Line = tuple[str, str, str]
Coord = tuple[int, int]


def is_valid_position(board: tuple[Line, Line, Line]) -> bool:
    flatten = [cell for line in board for cell in line]

    p1 = flatten.count('O')
    p2 = flatten.count('X')
    if p2 != p1 and (p1 + 1 != p2):
        return False

    wins = set()
    winner = None

    for (x, y), (dx, dy) in (
        ((0, 0), (1, 0)),
        ((0, 1), (1, 0)),
        ((0, 2), (1, 0)),
        ((0, 0), (0, 1)),
        ((1, 0), (0, 1)),
        ((2, 0), (0, 1)),
        ((0, 0), (1, 1)),
        ((2, 0), (-1, 1)),
    ):
        chks = [(x + i * dx, y + i * dy) for i in range(3)]

        for c in "OX":
            if all(board[y][x] == c for (x, y) in chks):
                wins.update(chks)
                winner = c

    if len(wins) not in {0,3,5}:
        return False

    return {
        'O': p1 == p2,
        'X': p1 != p2,
        None: True
    }[winner]
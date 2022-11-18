"""Kata url: https://www.codewars.com/kata/5779624bae28070489000146."""


def propagate(out, x, y, d=0):
    if x < 0 or x >= len(out[0]):
        return

    if y < 0 or y >= len(out):
        return

    if 0 <= out[y][x] <= d:
        return

    out[y][x] = d
    propagate(out, x - 1, y, d + 1)
    propagate(out, x + 1, y, d + 1)
    propagate(out, x, y - 1, d + 1)
    propagate(out, x, y + 1, d + 1)


def logistic_map(width, height, xs, ys):
    if not xs or not ys:
        return [[None] * width for _ in range(height)]

    out = [[-1 for _ in range(width)] for _ in range(height)]
    for x, y in zip(xs, ys):
        propagate(out, x, y)

    return out


def test_logistic_map():
    assert logistic_map(2, 2, [], []) == [[None, None], [None, None]]
    assert logistic_map(3, 3, [0], [0]) == [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
    assert logistic_map(3, 3, [2], [2]) == [[4, 3, 2], [3, 2, 1], [2, 1, 0]]
    assert logistic_map(1, 1, [0], [0]) == [[0]]
    assert logistic_map(5, 2, [0, 4], [0, 0]) == [
        [0, 1, 2, 1, 0], [1, 2, 3, 2, 1]
    ]

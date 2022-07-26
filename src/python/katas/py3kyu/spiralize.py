"""Kata url: https://www.codewars.com/kata/534e01fbbb17187c7e0000c6."""


def spiralize(size):
    canvas = [[0] * size for _ in range(size - 1)]

    for c, line_size in enumerate(range(size - 1, 0, -4)):
        offset = c * 2

        for i in range(line_size):
            canvas[i + offset][-(offset + 1)] = 1
            canvas[-(offset + 1)][i + offset] = 1

        for i in range(line_size - 2):
            canvas[i + (offset + 1)][offset] = 1
            canvas[offset + 1][i + (offset + 1)] = 1

    if not size % 2:
        canvas[size // 2 - 1][size // 2 - 1] = 0
    return [[1] * size] + canvas


def test_spiral():
    assert spiralize(5) == [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]

    assert spiralize(8) == [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]

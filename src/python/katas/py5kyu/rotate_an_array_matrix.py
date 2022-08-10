"""Kata url: https://www.codewars.com/kata/525a566985a9a47bc8000670."""
from typing import List

Matrix = List[List[int]]


def rotate(matrix: Matrix, direction: str) -> Matrix:
    out = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    for y, line in enumerate(matrix):
        for x, item in enumerate(line):
            out[x][y] = item

    return (
        out[::-1]
        if direction.startswith('counter-') else
        [line[::-1] for line in out]
    )


def test_rotate():
    c = 'clockwise'
    cc = 'counter-clockwise'

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    assert rotate(matrix, cc) == [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    assert rotate(matrix, c) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert rotate(rotate(matrix, cc), c) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    assert rotate(
        rotate(rotate(rotate(matrix, c), c), c), c
    ) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

    assert rotate(matrix, cc) == [[3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]]
    assert rotate(matrix, c) == [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]]

    matrix = [[1, 2, 3]]

    assert rotate(matrix, cc) == [[3], [2], [1]]
    assert rotate(matrix, c) == [[1], [2], [3]]
    assert rotate(rotate(matrix, c), c) == [[3, 2, 1]]

    matrix = [[1]]
    assert rotate(matrix, cc), [[1]]

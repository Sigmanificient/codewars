"""Kata url: https://www.codewars.com/kata/52fba2a9adcd10b34300094c."""


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def test_transpose():
    assert transpose([[1]]) == [[1]]
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]
    assert transpose(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert transpose(
        [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]
    ) == [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]]

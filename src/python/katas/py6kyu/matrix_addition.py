"""Kara url: https://www.codewars.com/kata/526233aefd4764272800036f."""


def matrix_addition(a, b):
    return [
        list(map(sum, zip(l1, l2)))
        for l1, l2 in zip(a, b)
    ]


def test_matrix_addition():
    assert matrix_addition(
        [[1, 2], [1, 2]], [[2, 3], [2, 3]]
    ) == [[3, 5], [3, 5]]

    assert matrix_addition([[1]], [[2]]) == [[3]]

    assert matrix_addition(
        [[1, 2, 3], [3, 2, 1],  [1, 1, 1]],
        [[2, 2, 1], [3, 2, 3], [1, 1, 3]]
    ) == [[3, 4, 4], [6, 4, 4], [2, 2, 4]]

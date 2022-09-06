"""Kata url: https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08."""


def multiplication_table(size):
    return [
        [line * x for x in range(1, size + 1)]
        for line in range(1, size + 1)
    ]


def test_multiplication_table():
    assert multiplication_table(2) == [[1, 2], [2, 4]]
    assert multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

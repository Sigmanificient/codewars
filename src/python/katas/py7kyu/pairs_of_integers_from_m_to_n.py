"""Kata url: https://www.codewars.com/kata/588e2a1ad1140d31cb00008c."""


def generate_pairs(m, n):
    return [
        (x, y)
        for x in range(m, n + 1)
        for y in range(x, n + 1)
    ]


def test_generate_pairs():
    assert generate_pairs(2, 4) == [
        (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)
    ]
    assert generate_pairs(0, 1) == [(0, 0), (0, 1), (1, 1)]
    assert generate_pairs(0, 0) == [(0, 0)]

"""Kata url: https://www.codewars.com/kata/515f51d438015969f7000013."""


def pyramid(n):
    return [[1] * i for i in range(1, n + 1)]


def test_pyramid():
    assert pyramid(0) == []
    assert pyramid(1) == [[1]]
    assert pyramid(2) == [[1], [1, 1]]
    assert pyramid(3) == [[1], [1, 1], [1, 1, 1]]

"""Kata url: https://www.codewars.com/kata/56453a12fcee9a6c4700009c."""


def close_compare(a: int | float, b: int | float, margin: float = 0):
    return (a - b - margin > 0) - (b - a - margin > 0)


def test_close_compare():
    assert close_compare(4, 5) == -1
    assert close_compare(5, 5) == 0
    assert close_compare(6, 5) == 1

    assert close_compare(2, 5, 3) == 0
    assert close_compare(5, 5, 3) == 0
    assert close_compare(8, 5, 3) == 0
    assert close_compare(8.1, 5, 3) == 1
    assert close_compare(1.99, 5, 3) == -1
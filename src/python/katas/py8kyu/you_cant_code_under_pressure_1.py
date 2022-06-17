"""Kata url: https://www.codewars.com/kata/53ee5429ba190077850011d4."""


def double_integer(i: int) -> int:
    return i * 2


def test_double_integer():
    assert double_integer(1) == 2
    assert double_integer(2) == 4
    assert double_integer(10) == 20

    assert double_integer(0) == 0
    assert double_integer(-1) == -2

"""Kata url: https://www.codewars.com/kata/54c27a33fb7da0db0100040e."""

from math import sqrt


def is_square(n: int) -> bool:
    return sqrt(n).is_integer() if n >= 0 else False


def test_is_square():
    assert is_square(0)
    assert is_square(4)
    assert is_square(25)
    assert not is_square(3)
    assert not is_square(-1)
    assert not is_square(26)

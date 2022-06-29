"""Kata url: https://www.codewars.com/kata/523b623152af8a30c6000027."""


def square(n: int) -> int:
    return n ** 2


def test_square():
    assert square(0) == 0
    assert square(1) == 1
    assert square(2) == 4
    assert square(50) == 2500

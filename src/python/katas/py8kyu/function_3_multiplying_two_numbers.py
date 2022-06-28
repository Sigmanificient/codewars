"""Kata url: https://www.codewars.com/kata/523b66342d0c301ae400003b."""


def multiply(a: int, b: int) -> int:
    return a * b


def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(1, -2) == -2
    assert multiply(3, 3) == 9
    assert multiply(3, -3) == -9

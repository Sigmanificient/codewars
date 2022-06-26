"""Kata url: https://www.codewars.com/kata/50654ddff44f800200000004."""


def multiply(a: int, b: int) -> int:
    return a * b


def test_multiply():
    assert multiply(1, 0) == 0
    assert multiply(1, -1) == -1

    assert multiply(2, 1) == 2
    assert multiply(2, 2) == 4
    assert multiply(2, 3) == 6
    assert multiply(99, 99) == 9801

"""Kata url: https://www.codewars.com/kata/55a5c82cd8e9baa49000004c."""


def divisible_count(x: int, y: int, k: int) -> int:
    return y // k - (x - 1) // k


def test_divisible_count():
    assert divisible_count(2, 4, 5) == 0
    assert divisible_count(6, 11, 2) == 3
    assert divisible_count(1, 22, 3) == 7
    assert divisible_count(1, 22, 4) == 5
    assert divisible_count(1, 22, 6) == 3

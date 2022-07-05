"""Kata url: https://www.codewars.com/kata/554b4ac871d6813a03000035."""

from typing import Tuple


def high_and_low(numbers_string: str) -> str:
    numbers: Tuple[int, ...] = tuple(map(int, numbers_string.split(' ')))
    return f"{max(numbers)} {min(numbers)}"


def test_high_and_low():
    assert high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9"
    assert high_and_low("1 2 3") == "3 1"

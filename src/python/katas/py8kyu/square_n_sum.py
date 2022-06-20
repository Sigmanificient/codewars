"""Kata url: https://www.codewars.com/kata/515e271a311df0350d00000f."""

from typing import List


def square_sum(numbers: List[int]) -> int:
    return sum(x ** 2 for x in numbers)


def test_square_sum():
    assert square_sum([1, 2]) == 5
    assert square_sum([0, 3, 4, 5]) == 50
    assert square_sum([]) == 0
    assert square_sum([-1, -2]) == 5
    assert square_sum([-1, 0, 1]) == 2

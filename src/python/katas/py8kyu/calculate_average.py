"""Kata url: https://www.codewars.com/kata/57a2013acf1fa5bfc4000921."""

from typing import List


def find_average(numbers: List[int]) -> float:
    return sum(numbers) / len(numbers)


def test_find_average():
    assert find_average([0, 100]) == 50
    assert find_average([0, 0, 0, 0, 5]) == 1
    assert find_average([1, 1, 1, 1]) == 1

    assert find_average([1, 2, 3]) == 2
    assert find_average([1, 5, 87, 45, 8, 4]) == 25

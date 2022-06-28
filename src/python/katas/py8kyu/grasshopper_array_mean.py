"""Kata url: https://www.codewars.com/kata/55d277882e139d0b6000005d."""

from typing import List


def find_average(nums: List[int]) -> float:
    return (sum(nums) / len(nums)) if nums else 0


def test_find_average():
    assert find_average([1]) == 1
    assert find_average([1, 3, 5, 7]) == 4
    assert find_average([-1, 3, 5, -7]) == 0
    assert find_average([5, 7, 3, 7]) == 5.5
    assert find_average([]) == 0

"""Kata url: https://www.codewars.com/kata/590e03aef55cab099a0002e8."""
from typing import List


def incrementer(nums: List[int]) -> List[int]:
    return [(x + c) % 10 for c, x in enumerate(nums, start=1)]


def test_incrementer():
    assert incrementer([]) == []
    assert incrementer([1, 2, 3]) == [2, 4, 6]
    assert incrementer([4, 6, 7, 1, 3]) == [5, 8, 0, 5, 8]
    assert incrementer([3, 6, 9, 8, 9]) == [4, 8, 2, 2, 4]
    assert incrementer([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8]) == [
        2,
        4,
        6,
        8,
        0,
        2,
        4,
        6,
        8,
        9,
        0,
        1,
        2,
        2,
    ]

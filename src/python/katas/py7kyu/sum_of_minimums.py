"""Kata url: https://www.codewars.com/kata/5d5ee4c35162d9001af7d699."""

from typing import List


def sum_of_minimums(numbers: List[List[int]]) -> int:
    return sum(map(min, numbers))


def test_sum_of_minimums():
    assert sum_of_minimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]]) == 9
    assert (
        sum_of_minimums(
            [[11, 12, 14, 54], [67, 89, 90, 56], [7, 9, 4, 3], [9, 8, 6, 7]]
        )
        == 76
    )

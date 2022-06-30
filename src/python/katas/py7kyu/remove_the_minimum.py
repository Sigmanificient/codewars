"""Kata url: https://www.codewars.com/kata/563cf89eb4747c5fb100001b."""

from typing import List


def remove_smallest(numbers: List[int]) -> List[int]:
    if not numbers:
        return []

    out = numbers[:]
    out.remove(min(numbers))
    return out


def test_remove_smallest():
    assert remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5]
    assert remove_smallest([5, 3, 2, 1, 4]) == [5, 3, 2, 4]
    assert remove_smallest([1, 2, 3, 1, 1]) == [2, 3, 1, 1]
    assert remove_smallest([1]) == []
    assert remove_smallest([]) == []

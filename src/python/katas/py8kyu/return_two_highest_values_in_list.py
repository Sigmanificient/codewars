"""Kata url: https://www.codewars.com/kata/57ab3c09bb994429df000a4a."""

from typing import List


def two_highest(arg1: List[int]) -> List[int]:
    return sorted(set(arg1), reverse=True)[:2]


def test_two_highest():
    assert two_highest([]) == []
    assert two_highest([1, 2, 3, 4, 5]) == [5, 4]
    assert two_highest([15, 20, 20, 17]) == [20, 17]
    assert two_highest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9]

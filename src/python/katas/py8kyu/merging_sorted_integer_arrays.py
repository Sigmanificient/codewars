"""Kata url: https://www.codewars.com/kata/573f5c61e7752709df0005d2."""

from typing import List


def merge_arrays(first: List[int], second: List[int]) -> List[int]:
    return sorted(set(first + second))


def test_merge_arrays():
    assert merge_arrays([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]        
    assert merge_arrays([2, 4, 8], [2, 4, 6]) == [2, 4, 6, 8]

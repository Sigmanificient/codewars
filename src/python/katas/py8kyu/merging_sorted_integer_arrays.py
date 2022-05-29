"""Kata url: https://www.codewars.com/kata/573f5c61e7752709df0005d2."""

from typing import List


def merge_arrays(first: List[int], second: List[int]) -> List[int]:
    return sorted(set(first + second))

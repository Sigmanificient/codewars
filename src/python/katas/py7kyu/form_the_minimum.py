"""Kata url: https://www.codewars.com/kata/5ac6932b2f317b96980000ca."""
from typing import List


def min_value(digits: List[int]) -> int:
    return int(''.join(map(str, sorted(set(digits)))))

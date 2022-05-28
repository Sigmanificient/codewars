"""Kata url: https://www.codewars.com/kata/58cb43f4256836ed95000f97."""

from typing import List


def mul(x: List[int]) -> int:
    """Multiply every element of an array together."""
    r = 1
    for k in x:
        r *= k
    return r


def find_difference(a: List[int], b: List[int]) -> int:
    return abs(mul(a) - mul(b))

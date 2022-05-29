"""Kata url: https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad."""

from typing import List


def invert(lst: List[int]) -> List[int]:
    return [-x for x in lst]

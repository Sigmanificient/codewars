"""Kata url: https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1."""

from typing import List


def array_madness(a: List[int], b: List[int]) -> bool:
    return sum(i ** 2 for i in a) > sum(j ** 3 for j in b)

"""Kata url: https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1."""

from typing import List


def array_madness(a: List[int], b: List[int]) -> bool:
    return sum(i ** 2 for i in a) > sum(j ** 3 for j in b)


def test_array_madness():
    assert array_madness([4, 5, 6], [1, 2, 3])
    assert not array_madness([1, 2, 3], [4, 5, 6])

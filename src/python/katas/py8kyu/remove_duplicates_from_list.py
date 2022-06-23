"""Kata url: https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118."""

from typing import List


def distinct(seq: List[int]) -> List[int]:
    return sorted(list(set(seq)), key=lambda x: seq.index(x))


def test_distinct():
    assert distinct([1]) == [1]
    assert distinct([1, 2]) == [1, 2]
    assert distinct([1, 1, 2]) == [1, 2]
    assert distinct([1, 1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]) == [1, 2, 3, 4, 5, 6, 7]

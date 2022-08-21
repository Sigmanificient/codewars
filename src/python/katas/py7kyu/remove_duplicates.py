"""Kata url: https://www.codewars.com/kata/53e30ec0116393fe1a00060b."""
from typing import List


def unique(integers: List[int]) -> List[int]:
    return sorted(set(integers), key=integers.index)


def test_unique():
    assert unique([]) == []
    assert unique([-1]) == [-1]
    assert unique([-1, 5, 10, -100, 3, 2]) == [-1, 5, 10, -100, 3, 2]
    assert unique([1, 2, 3, 3, 2, 1, 2, 3, 1, 1, 3, 2]) == [1, 2, 3]
    assert unique([1, 3, 2, 3, 2, 1, 2, 3, 1, 1, 3, 2]) == [1, 3, 2]
    assert unique([3, 2, 3, 3, 2, 1, 2, 3, 1, 1, 3, 2]) == [3, 2, 1]

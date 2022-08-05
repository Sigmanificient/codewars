"""Kata url: https://www.codewars.com/kata/544a54fd18b8e06d240005c0."""
from typing import List


def find_smallest(numbers: List[int], to_return: str) -> int:
    m = min(numbers)
    return numbers.index(m) if to_return == "index" else m


def test_find_smallest():
    assert find_smallest([5, 4, 3, 2, 1], "value") == 1
    assert find_smallest([5, 4, 3, 2, 1], "index") == 4
    assert find_smallest([8, 0, 9], "index") == 1
    assert find_smallest([8, 0, 9], "value") == 0
    assert find_smallest([1, 1, 0, 0, 1, 1], "value") == 0
    assert find_smallest([1, 1, 0, 0, 1, 1], "index") == 2

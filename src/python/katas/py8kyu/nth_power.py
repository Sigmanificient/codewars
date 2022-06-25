"""Kata url: https://www.codewars.com/kata/57d814e4950d8489720008db."""

from typing import List


def index(array: List[int], n: int) -> int:
    return array[n] ** n if (len(array) > n) else -1


def test_index():
    assert index([1, 2, 3, 4], 2) == 9
    assert index([1, 3, 10, 100], 3) == 1000000
    assert index([1, 3, 10, 100], 4) == -1

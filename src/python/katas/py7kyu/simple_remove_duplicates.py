"""Kata url: https://www.codewars.com/kata/5ba38ba180824a86850000f7."""
from typing import List


def solve(arr: List[int]) -> List[int]:
    cache = set()
    out = []

    for item in arr[::-1]:
        if item in cache:
            continue

        cache.add(item)
        out.append(item)

    return out[::-1]


def test_solve():
    assert solve([3, 4, 4, 3, 6, 3]) == [4, 6, 3]
    assert solve([1, 2, 1, 2, 1, 2, 3]) == [1, 2, 3]
    assert solve([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert solve([1, 1, 4, 5, 1, 2, 1]) == [4, 5, 2, 1]

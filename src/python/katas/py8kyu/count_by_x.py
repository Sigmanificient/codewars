"""Kata url: https://www.codewars.com/kata/5513795bd3fafb56c200049e."""

from typing import List


def count_by(x: int, n: int) -> List[int]:
    return list(range(x, x * n + 1, x))


def test_count_by():
    assert count_by(1, 5) == [1, 2, 3, 4, 5]
    assert count_by(2, 5) == [2, 4, 6, 8, 10]
    assert count_by(3, 5) == [3, 6, 9, 12, 15]
    assert count_by(50, 5) == [50, 100, 150, 200, 250]
    assert count_by(100, 5) == [100, 200, 300, 400, 500]

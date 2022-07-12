"""Kata url: https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0."""

from typing import List


def solution(n: int, d: int) -> List[int]:
    return [] if d <= 0 else [int(k) for k in str(n)[-d:]]


def test_solution():
    assert solution(1, 1) == [1]
    assert solution(123767, 4) == [3, 7, 6, 7]
    assert solution(0, 1) == [0]
    assert solution(34625647867585, 10) == [5, 6, 4, 7, 8, 6, 7, 5, 8, 5]

    assert solution(1234, 0) == []
    assert solution(24134, -4) == []

    assert solution(1343, 5) == [1, 3, 4, 3]

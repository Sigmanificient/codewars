"""Kata url: https://www.codewars.com/kata/5174a4c0f2769dd8b1000003."""

from typing import Optional, List


def solution(nums: Optional[List[int]]) -> List[int]:
    return sorted(nums) if nums is not None else []


def test_solution():
    assert solution([]) == []
    assert solution(None) == []
    assert solution([1, 2, 3, 10, 5]) == [1, 2, 3, 5, 10]
    assert solution([20, 2, 10]) == [2, 10, 20]
    assert solution([2, 20, 10]) == [2, 10, 20]

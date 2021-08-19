"""Kata url: https://www.codewars.com/kata/5174a4c0f2769dd8b1000003."""

from typing import Optional, List


def solution(nums: Optional[List[int]]) -> List[int]:
    return sorted(nums) if nums is not None else []

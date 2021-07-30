"""Kata url: https://www.codewars.com/kata/56b29582461215098d00000f."""

from typing import List


def pipe_fix(nums: List[int]) -> List[int]:
    return list(range(nums[0], nums[-1] + 1))

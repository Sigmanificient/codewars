"""Kata url: https://www.codewars.com/kata/56b29582461215098d00000f."""

from typing import List


def pipe_fix(nums: List[int]) -> List[int]:
    return list(range(nums[0], nums[-1] + 1))


def test_pipe_fix():
    assert pipe_fix([1, 2, 3, 5, 6, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert pipe_fix([1, 2, 3, 12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert pipe_fix([6, 9]) == [6, 7, 8, 9]
    assert pipe_fix([-1, 4]) == [-1, 0, 1, 2, 3, 4]
    assert pipe_fix([1, 2, 3]) == [1, 2, 3]

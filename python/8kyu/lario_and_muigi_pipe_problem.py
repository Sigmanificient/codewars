from typing import List


def pipe_fix(nums: List[int]) -> List[int]:
    """Kata url: https://www.codewars.com/kata/56b29582461215098d00000f."""
    return list(range(nums[0], nums[-1] + 1))

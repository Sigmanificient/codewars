from typing import Optional, List


def solution(nums: Optional[List[int]]) -> List[int]:
    return sorted(nums) if nums is not None else []

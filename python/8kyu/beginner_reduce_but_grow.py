from typing import List


def grow(arr: List[int]) -> int:
    """Kata url: https://www.codewars.com/kata/57f780909f7e8e3183000078."""
    a: int = 1
    for b in arr:
        a *= b
    return a

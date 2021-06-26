from typing import List


def check_exam(arr1: List[str], arr2: List[str]) -> int:
    """Kata url: https://www.codewars.com/kata/5a3dd29055519e23ec000074."""
    return max(0, sum((-1 if x != y else 4) if y else 0 for x, y in zip(arr1, arr2)))

from typing import List


def flip(d: str, a: List[int]) -> List[int]:
    """Kata url: https://www.codewars.com/kata/5f70c883e10f9e0001c89673."""
    return sorted(a)[::-1 if d == 'L' else 1]

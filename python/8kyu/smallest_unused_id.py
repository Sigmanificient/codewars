from typing import List


def next_id(arr: List[int]) -> int:
    """Kata url: https://www.codewars.com/kata/55eea63119278d571d00006a."""
    c: int = 0

    for item in sorted(set(arr)):
        if item != c:
            return c
        c += 1
    else:
        return c

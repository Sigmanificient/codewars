"""Kata url: https://www.codewars.com/kata/54d4c8b08776e4ad92000835."""

from typing import Optional, List


def isPP(n: int) -> Optional[List[int]]:
    possibles = [
        i for i in range(2, min(n - 1, 1001)) if (n / i).is_integer()
    ]

    if not possibles:
        return None

    for possible in possibles:
        c, x = 1, 0

        while x < n:
            x = possible ** c
            c += 1

        if x == n:
            return [possible, c - 1]

    return None

"""Kata url: https://www.codewars.com/kata/56269eb78ad2e4ced1000013."""

import math


def find_next_square(sq: int) -> int:
    r: float = math.sqrt(sq)

    return -1 if r % 1 else (r + 1) ** 2

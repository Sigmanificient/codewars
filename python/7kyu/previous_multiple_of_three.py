"""Kata url: https://www.codewars.com/kata/61123a6f2446320021db987d."""

from typing import Optional


def prev_mult_of_three(n: int) -> Optional[int]:
    while n % 3:
        n //= 10

    return n or None

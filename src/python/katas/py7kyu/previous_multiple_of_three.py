"""Kata url: https://www.codewars.com/kata/61123a6f2446320021db987d."""

from typing import Optional


def prev_mult_of_three(n: int) -> Optional[int]:
    while n % 3:
        n //= 10

    return n or None


def test_prev_mult_of_three():
    assert prev_mult_of_three(1) is None
    assert prev_mult_of_three(25) is None
    assert prev_mult_of_three(36) == 36
    assert prev_mult_of_three(1244) == 12
    assert prev_mult_of_three(952406) == 9

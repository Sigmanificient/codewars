"""Kata url: https://www.codewars.com/kata/576400f2f716ca816d001614."""

from math import gcd
from typing import Tuple


def reduce_fraction(fraction: Tuple[int, int]) -> Tuple[int, int]:
    n, d = fraction

    while (g := gcd(n, d)) > 1:
        n //= g
        d //= g

    return n, d


def test_reduce_fraction():
    assert reduce_fraction((60, 20)) == (3, 1)
    assert reduce_fraction((80, 120)) == (2, 3)
    assert reduce_fraction((4, 2)) == (2, 1)
    assert reduce_fraction((45, 120)) == (3, 8)
    assert reduce_fraction((1000, 1)) == (1000, 1)
    assert reduce_fraction((1, 1)) == (1, 1)
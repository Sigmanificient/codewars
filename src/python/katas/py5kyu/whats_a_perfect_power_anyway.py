"""Kata url: https://www.codewars.com/kata/54d4c8b08776e4ad92000835."""
from math import floor, log
from random import random, randrange
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


def test_isPP():
    pp = [
        4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169,
        196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484
    ]

    for item in pp:
        assert isPP(item) is not None

    for _ in range(100):
        m = 2 + floor(random() * 255)
        k = 2 + floor(random() * log(268435455) / log(m))
        l = m ** k
        r = isPP(l)

        assert r is not None
        assert r[0]**r[1] == l

"""Kata url: https://www.codewars.com/kata/55aa075506463dac6600010d."""

from math import sqrt
from typing import List

cache = {}


def list_squared(m: int, n: int) -> List[List[int]]:
    out = []

    for i in range(m, n + 1):
        k = cache.get(i, -1)
        if k != -1:
            if k:
                out.append([i, k])
            continue

        s = sum(x**2 for x in range(1, i + 1) if not i % x)

        if not sqrt(s) % 1:
            out.append([i, s])
            cache[i] = s

        else:
            cache[i] = 0

    return out


def test_list_square():
    assert list_squared(1, 250) == [[1, 1], [42, 2500], [246, 84100]]
    assert list_squared(42, 250) == [[42, 2500], [246, 84100]]
    assert list_squared(250, 500) == [[287, 84100]]
    assert list_squared(300, 600) == []
    assert list_squared(600, 1500) == [[728, 722500], [1434, 2856100]]
    assert list_squared(1500, 1800) == [[1673, 2856100]]
    assert list_squared(1800, 2000) == [[1880, 4884100]]
    assert list_squared(2000, 2200) == []

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

        s = sum(x ** 2 for x in range(1, i + 1) if not i % x)

        if not sqrt(s) % 1:
            out.append([i, s])
            cache[i] = s

        else:
            cache[i] = 0

    return out

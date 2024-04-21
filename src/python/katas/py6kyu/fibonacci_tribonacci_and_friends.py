"""Kata url: https://www.codewars.com/kata/556e0fccc392c527f20000c5."""
from typing import List


def xbonacci(signature: List[int], n: int) -> List[int]:
    i = k = 0

    mem = signature
    out = mem[:]

    if n < len(mem):
        return mem[:n]

    for _ in range(n - len(mem)):
        k = sum(mem)
        out.append(k)

        mem[i] = k
        i = (i + 1) % len(mem)

    return out


def test_xbonacci():
    assert xbonacci([0, 1], 10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert xbonacci([1, 1], 10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert xbonacci([0, 0, 0, 0, 1], 10) == [0, 0, 0, 0, 1, 1, 2, 4, 8, 16]
    assert xbonacci([1, 0, 0, 0, 0, 0, 1], 10) == [1, 0, 0, 0, 0, 0, 1, 2, 3, 6]
    assert xbonacci([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 20) == [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        1, 2, 4, 8, 16, 32, 64, 128, 256
    ]
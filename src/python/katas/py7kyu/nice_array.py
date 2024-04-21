"""Kata url: https://www.codewars.com/kata/59b844528bcb7735560000a0."""

from typing import List


def is_nice(arr: List[int]) -> bool:
    t = sorted(set(arr))

    if not t:
        return False

    ts = len(t)
    for c, i in enumerate(t):
        p = t[c - 1]
        n = t[(c + 1) if (c + 1) < ts else c]

        if (i + 1 != n) and ((i - 1) != p):
            return False

    return True


def test_is_nice():
    assert is_nice([2, 10, 9, 3])
    assert not is_nice([3, 4, 5, 7])
    assert not is_nice([])
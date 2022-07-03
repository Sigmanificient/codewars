"""Kata url: https://www.codewars.com/kata/5270d0d18625160ada0000e4."""

from collections import Counter


def score(dice):
    c, t = Counter(dice), 0

    for k, v in c.items():
        if v >= 3:
            t += 1000 if k == 1 else k * 100
            c[k] -= 3

    return t + (100 * c.get(1, 0)) + (50 * c.get(5, 0))


def test_score():
    assert score([2, 3, 4, 6, 2]) == 0
    assert score([4, 4, 4, 3, 3]) == 400
    assert score([2, 4, 4, 5, 4]) == 450

"""Kata url: https://www.codewars.com/kata/5b68c7029756802aa2000176."""
from math import log


def logs(x, a, b):
    return log(a, x) + log(b, x)


def test_logs():
    assert round(logs(10, 2, 3), 5) == 0.77815
    assert round(logs(5, 2, 3), 5) == 1.11328
    assert round(logs(1000, 2, 3), 5) == 0.25938

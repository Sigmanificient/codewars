"""Kata url: https://www.codewars.com/kata/596f72bbe7cd7296d1000029."""


def deep_count(a, d=0):
    if isinstance(a, list):
        return sum((deep_count(b, 1) for b in a), bool(d))
    return 1


def test_deep_count():
    assert deep_count([]) == 0
    assert deep_count([1, 2, 3]) == 3
    assert deep_count(["x", "y", ["z"]]) == 4
    assert deep_count([1, 2, [3, 4, [5]]]) == 7
    assert deep_count([[[[[[[[[]]]]]]]]]) == 8

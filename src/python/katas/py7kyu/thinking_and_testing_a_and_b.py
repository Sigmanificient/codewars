"""Kata url: https://www.codewars.com/kata/56d904db9963e9cf5000037d."""


def _testit(a, b):
    return a | b


def test_testit():
    assert _testit(0, 1) == 1
    assert _testit(1, 2) == 3
    assert _testit(10, 20) == 30
    assert _testit(1, 1) == 1
    assert _testit(1, 3) == 3

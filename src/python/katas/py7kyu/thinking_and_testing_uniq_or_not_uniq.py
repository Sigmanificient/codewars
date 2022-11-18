"""Kata url: https://www.codewars.com/kata/56d93f249c844788bc000002."""


def _testit(a, b):
    a = list(set(a))
    b = list(set(b))
    return sorted(a + b)


def test_testit():
    assert _testit([0], [1]) == [0, 1]
    assert _testit([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert _testit([1], [2, 3, 4]) == [1, 2, 3, 4]
    assert _testit([1, 2, 3], [4]) == [1, 2, 3, 4]
    assert _testit([1, 2], [1, 2]) == [1, 1, 2, 2]

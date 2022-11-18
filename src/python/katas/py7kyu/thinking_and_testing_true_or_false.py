"""Kata url: https://www.codewars.com/kata/56d931ecc443d475d5000003."""


def _testit(n):
    return f'{n:b}'.count('1')


def test_testit():
    assert _testit(0) == 0
    assert _testit(0) == 0
    assert _testit(2) == 1
    assert _testit(3) == 2
    assert _testit(4) == 1
    assert _testit(5) == 2
    assert _testit(6) == 2
    assert _testit(7) == 3
    assert _testit(8) == 1
    assert _testit(9) == 2
    assert _testit(10) == 2
    assert _testit(100) == 3
    assert _testit(1000) == 6
    assert _testit(10000) == 5

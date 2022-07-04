"""Kata url: https://www.codewars.com/kata/59342039eb450e39970000a6."""


def odd_count(n: int) -> int:
    return n // 2


def test_odd_count():
    assert odd_count(15) == 7
    assert odd_count(15023) == 7511
    assert odd_count(0) == 0

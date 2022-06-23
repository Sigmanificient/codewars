"""Kata url: https://www.codewars.com/kata/5ce9c1000bab0b001134f5af."""

from math import ceil


def quarter_of(month: int) -> int:
    return ceil(month / 3)


def test_quarter_of():
    assert quarter_of(3) == 1
    assert quarter_of(8) == 3
    assert quarter_of(11) == 4

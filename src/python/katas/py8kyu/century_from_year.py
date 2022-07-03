"""Kata url: https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097."""

from math import ceil


def century(year: int) -> int:
    return ceil(year / 100)


def test_century():
    assert century(89) == 1
    assert century(1705) == 18
    assert century(1900) == 19
    assert century(1601) == 17
    assert century(2000) == 20
    assert century(356) == 4

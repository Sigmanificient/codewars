"""Kata url: https://www.codewars.com/kata/59441520102eaa25260000bf."""


def unusual_five() -> int:
    return sum([True, True, True, True, True])


def test_unusual_five():
    assert unusual_five() == 5

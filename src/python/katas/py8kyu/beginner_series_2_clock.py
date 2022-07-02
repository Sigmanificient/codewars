"""Kata url: https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a."""


def past(h: int, m: int, s: int) -> int:
    return (h * 3600 + m * 60 + s) * 1000


def test_past():
    assert past(0, 1, 1) == 61000
    assert past(1, 1, 1) == 3661000
    assert past(0, 0, 0) == 0
    assert past(1, 0, 1) == 3601000
    assert past(1, 0, 0) == 3600000
    assert past(0, 1, 0) == 60000

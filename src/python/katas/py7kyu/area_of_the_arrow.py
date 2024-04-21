"""Kata url: https://www.codewars.com/kata/589478160c0f8a40870000bc."""


def arrow_area(a: int, b: int) -> int | float:
    return (a * b) / 4


def test_arrow_area():
    assert arrow_area(4, 2) == 2
    assert (arrow_area(7, 6) - 10.5) < 0.0001
    assert (arrow_area(25, 25) - 156.25) < 0.0001
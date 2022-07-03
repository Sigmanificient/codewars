"""Kata url: https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd."""


def paperwork(n: int, m: int) -> int:
    return 0 if n < 0 or m < 0 else n * m


def test_paperwork():
    assert paperwork(5, 5) == 25
    assert paperwork(-5, 5) == 0
    assert paperwork(5, -5) == 0
    assert paperwork(-5, -5) == 0
    assert paperwork(5, 0) == 0

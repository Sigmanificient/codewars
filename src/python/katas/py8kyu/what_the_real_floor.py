"""Kata url: https://www.codewars.com/kata/574b3b1599d8f897470018f6."""


def get_real_floor(n: int) -> int:
    if n <= 0:
        return n

    return n - 1 if n < 13 else n - 2


def test_get_real_floor():
    assert get_real_floor(1) == 0
    assert get_real_floor(5) == 4
    assert get_real_floor(15) == 13

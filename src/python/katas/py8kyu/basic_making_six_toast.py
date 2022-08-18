"""Kata url: https://www.codewars.com/kata/5834fec22fb0ba7d080000e8."""


def six_toast(num: int) -> int:
    return abs(6 - num)


def test_six_toast():
    assert six_toast(15) == 9
    assert six_toast(6) == 0
    assert six_toast(3) == 3

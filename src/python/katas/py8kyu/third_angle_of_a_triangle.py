"""Kata url: https://www.codewars.com/kata/5a023c426975981341000014."""


def other_angle(a: int, b: int) -> int:
    return 180 - (a + b)


def test_other_angle():
    assert other_angle(30, 60) == 90
    assert other_angle(60, 60) == 60
    assert other_angle(43, 78) == 59
    assert other_angle(10, 20) == 150

"""Kata url: https://www.codewars.com/kata/55d24f55d7dd296eb9000030."""


def summation(num: int) -> int:
    return sum(range(1, num + 1))


def test_summation():
    assert summation(1) == 1
    assert summation(8) == 36
    assert summation(22) == 253
    assert summation(100) == 5050
    assert summation(213) == 22791

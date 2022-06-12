"""Kata url: https://www.codewars.com/kata/5467e4d82edf8bbf40000155."""


def descending_order(num: int) -> int:
    return int(''.join(sorted(str(num), reverse=True)))


def test_order():
    assert descending_order(0) == 0
    assert descending_order(15) == 51
    assert descending_order(123456789) == 987654321

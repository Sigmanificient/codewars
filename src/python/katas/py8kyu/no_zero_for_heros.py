"""Kata url: https://www.codewars.com/kata/570a6a46455d08ff8d001002."""


def no_boring_zeros(n: int) -> int:
    if n == 0:
        return 0

    while not n % 10:
        n //= 10
    return n


def test_no_boring_zeros():
    assert no_boring_zeros(0) == 0
    assert no_boring_zeros(1450) == 145
    assert no_boring_zeros(960000) == 96
    assert no_boring_zeros(1050) == 105
    assert no_boring_zeros(-1050) == -105
    assert no_boring_zeros(2016) == 2016

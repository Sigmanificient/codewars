"""Kata url: https://www.codewars.com/kata/542c0f198e077084c0000c2e."""


def divisors(n: int) -> int:
    return sum(n % x == 0 for x in range(1, n + 1))


def test_divisors():
    assert divisors(1) == 1
    assert divisors(4) == 3
    assert divisors(5) == 2
    assert divisors(12) == 6
    assert divisors(30) == 8
    assert divisors(4096) == 13

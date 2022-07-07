"""Kata url: https://www.codewars.com/kata/542c0f198e077084c0000c2e."""


def divisors(n: int) -> int:
    return sum(n % x == 0 for x in range(1, n + 1))

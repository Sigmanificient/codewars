"""Kata url: https://www.codewars.com/kata/57f36495c0bb25ecf50000e7."""


def find(n: int) -> int:
    return sum(k for k in range(n + 1) if not (k % 3 and k % 5))

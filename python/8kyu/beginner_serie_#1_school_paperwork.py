"""Kata url: https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd."""


def paperwork(n: int, m: int) -> int:
    if n < 0 or m < 0:
        return 0

    return n * m

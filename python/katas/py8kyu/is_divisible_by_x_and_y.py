"""Kata url: https://www.codewars.com/kata/5545f109004975ea66000086."""


def is_divisible(n: int, x: int, y: int) -> bool:
    return (n / x).is_integer() and (n / y).is_integer()

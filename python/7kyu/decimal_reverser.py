"""Kata url: https://www.codewars.com/kata/60cf559c068ae600468f8e5a."""


def reverse_float_decimal(n: float) -> float:
    return int(n) + float('0.' + str(round(n % 1, 5))[2:][::-1])

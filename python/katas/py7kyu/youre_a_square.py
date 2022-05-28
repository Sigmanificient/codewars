"""Kata url: https://www.codewars.com/kata/54c27a33fb7da0db0100040e."""

from math import sqrt


def is_square(n: int) -> bool:
    return sqrt(n).is_integer() if n >= 0 else False

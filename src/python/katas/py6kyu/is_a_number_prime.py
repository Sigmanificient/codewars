"""Kata url: https://www.codewars.com/kata/5262119038c0985a5b00029f."""

from math import sqrt


def is_prime(num):
    if num < 3:
        return num == 2

    return num % 2 and all(
        num % n
        for n in range(3, int(sqrt(num) + 1), 2)
    )

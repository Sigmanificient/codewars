"""Kata url: https://www.codewars.com/kata/53daa9e5af55c184db00025f."""

import math


def is_prime(n: int) -> bool:
    if n in {2, 3}:
        return True

    if n < 3 or not n % 2:
        return False

    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

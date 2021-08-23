# Kata url: https://www.codewars.com/kata/5539fecef69c483c5a000015.

from math import sqrt
from typing import List


def is_not_pal_prime(n) -> bool:
    if n == 3:
        return False

    if not n % 2:
        return False

    if str(n) == str(n)[::-1]:
        return False

    return all(n % d for d in range(3, int(sqrt(n)) + 1, 2))


def backwards_prime(start: int, stop: int) -> List[int]:
    if not start % 2:
        start += 1

    return [
        i for i in range(start, stop + 1, 2)
        if is_not_pal_prime(i) and is_not_pal_prime(int(str(i)[::-1]))
    ]

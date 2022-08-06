"""Kata url: https://www.codewars.com/kata/537ba77315ddd92659000fec."""
from math import sqrt, ceil
from typing import List


def is_prime(n: int) -> bool:
    if n in {2, 3}:
        return True

    if n < 2 or not n % 2:
        return False

    return all(n % i for i in range(3, ceil(sqrt(n)) + 1, 2))


def check_goldbach(number: int) -> List[int]:
    if number < 2 or number % 2:
        return []

    for a in range(number // 2 + 1):
        if not is_prime(a):
            continue

        b = number - a
        if is_prime(b):
            return [a, b]

    return []


def test_goldbach():
    assert check_goldbach(2) == []
    assert check_goldbach(15) == []
    assert check_goldbach(4) == [2, 2]
    assert check_goldbach(8) == [3, 5]
    assert check_goldbach(10) == [3, 7]
    assert check_goldbach(24) == [5, 19]
    assert check_goldbach(100) == [3, 97]
    assert check_goldbach(1234) == [3, 1231]

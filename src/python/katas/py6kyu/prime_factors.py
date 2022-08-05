"""Kata url: https://www.codewars.com/kata/542f3d5fd002f86efc00081a."""

from math import sqrt, ceil
from typing import Generator, List


def is_prime(n: int) -> bool:
    if n < 2 or not n % 2:
        return False

    if n in {2, 3}:
        return True

    return all(n % i for i in range(3, ceil(sqrt(n)) + 1, 2))


def primes() -> Generator[int, None, None]:
    yield 2
    yield 3

    k = 5
    while True:
        if is_prime(k):
            yield k

        k += 2


def prime_factors(n: int) -> List[int]:
    factors = []
    prime = primes()

    while n != 1 and not is_prime(n):
        p = next(prime)

        if n % p:
            continue

        factors.append(p)
        prime = primes()
        n //= p

    if n > 1:
        factors.append(n)

    return factors


def test_prime_factors():
    assert prime_factors(1) == []
    assert prime_factors(4) == [2, 2]
    assert prime_factors(3) == [3]
    assert prime_factors(6) == [2, 3]
    assert prime_factors(9) == [3, 3]
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(11020332) == [2, 2, 3, 918361]

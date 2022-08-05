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


def test_prime_gen():
    p = primes()

    assert [next(p) for _ in range(100)] == [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97,  101, 103, 107, 109, 113, 127, 131, 137, 139,
        149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
        227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
        307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383,
        389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
        467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
    ]

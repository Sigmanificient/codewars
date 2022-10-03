"""Kata url: https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124."""
import math


def is_prime(n: int) -> bool:
    if n < 2 or not n % 2:
        return False

    if n in {2, 3}:
        return True

    return all(n % i for i in range(3, math.ceil(math.sqrt(n)) + 1, 2))


def primes():
    yield 2
    yield 3

    k = 5
    while True:
        if is_prime(k):
            yield k

        k += 2


def num_primorial(n):
    prime = primes()

    t = 1
    for _ in range(n):
        t *= next(prime)

    return t


def test_primorial():
    assert num_primorial(3) == 30
    assert num_primorial(4) == 210
    assert num_primorial(5) == 2310
    assert num_primorial(8) == 9699690
    assert num_primorial(9) == 223092870

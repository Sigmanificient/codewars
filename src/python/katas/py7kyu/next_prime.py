"""Kata url: https://www.codewars.com/kata/58e230e5e24dde0996000070."""

from math import ceil, sqrt


def is_prime(n):
    return all(n % i for i in range(3, ceil(sqrt(n)) + 1, 2))


def next_prime(n):
    if n < 2:
        return 2

    if n == 2:
        return 3

    n += (n % 2) + 1
    while not is_prime(n):
        n += 2

    return n


def test_next_primes():
    assert is_prime(0) == 2
    assert is_prime(2) == 3
    assert is_prime(3) == 5
    assert is_prime(13) == 17
    assert is_prime(181) == 191
    assert is_prime(911) == 919

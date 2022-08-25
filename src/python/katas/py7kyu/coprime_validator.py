"""Kata url: https://www.codewars.com/kata/585c50e75d0930e6a7000336."""
from math import sqrt


def get_prime_factors(n):
    result = []
    for i in range(2, int(sqrt(n)) + 1):
        while not n % i:
            result.append(i)
            n //= i

    if n > 1:
        result.append(n)

    return result


def are_coprime(n, m):
    fac_n = set(get_prime_factors(n))
    fac_m = set(get_prime_factors(m))

    return len(fac_n) + len(fac_m) == len(fac_n | fac_m)


def test_are_coprime():
    assert are_coprime(20, 27)
    assert not are_coprime(12, 39)
    assert not are_coprime(17, 34)
    assert not are_coprime(34, 17)
    assert not are_coprime(35, 10)
    assert are_coprime(64, 27)

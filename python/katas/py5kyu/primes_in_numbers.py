"""Kata url: https://www.codewars.com/kata/54d512e62a5e54c96200019e."""
from math import sqrt


def prime_factors(n: int) -> str:
    factors = get_prime_factors(n)

    primes_factorisation = [
        f'({prime}**{factors.count(prime)})'
        if factors.count(prime) > 1 else f'({prime})'
        for prime in sorted(set(factors))
    ]

    return ''.join(primes_factorisation)


def get_prime_factors(n):
    result = []
    for i in range(2, int(sqrt(n)) + 1):
        while not n % i:
            result.append(i)
            n //= i

    if n > 1:
        result.append(n)

    return result

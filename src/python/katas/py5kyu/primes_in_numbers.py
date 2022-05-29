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


def test_prime_factors():
    assert prime_factors(25) == '(5**2)'
    assert prime_factors(7 * 5) == '(5)(7)'
    assert prime_factors(100) == '(2**2)(5**2)'
    assert prime_factors(3301) == '(3301)'
    assert prime_factors(7775460) == "(2**2)(3**3)(5)(7)(11**2)(17)"


def test_get_prime_factors():
    assert get_prime_factors(25) == [5, 5]
    assert get_prime_factors(7 * 5) == [5, 7]
    assert get_prime_factors(100) == [2, 2, 5, 5]
    assert get_prime_factors(3301) == [3301]
    assert get_prime_factors(7775460) == [2, 2, 3, 3, 3, 5, 7, 11, 11, 17]

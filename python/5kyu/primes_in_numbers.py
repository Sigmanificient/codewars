from math import sqrt


def prime_factors(n: int) -> str:
    """ """
    result = []
    for i in range(2, int(sqrt(n)) + 1):
        while not n % i:
            result.append(i)
            n //= i

    if n > 1:
        result.append(n)

    primes_factorisation = []
    for prime in sorted(set(result)):
        power = result.count(prime)

        if power > 1:
            primes_factorisation.append(f'({prime}**{result.count(prime)})')
        else:
            primes_factorisation.append(f'({prime})')

    return ''.join(primes_factorisation)

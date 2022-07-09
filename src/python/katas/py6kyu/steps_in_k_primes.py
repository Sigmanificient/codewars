from math import sqrt


def get_count_prime_factors(n):
    c = 0
    for i in range(2, int(sqrt(n)) + 1):
        while not n % i:
            c += 1
            n //= i

    if n > 1:
        c += 1

    return c


def k_primes_step(k, step, start, nd):
    out = [
        i for i in range(start, nd + 1)
        if get_count_prime_factors(i) == k
    ]

    return [
        [x, x + step] for x, n in zip(out, out[1::])
        if x + step in out
    ]


def test_get_prime_factors():
    assert get_count_prime_factors(25) == 2
    assert get_count_prime_factors(7 * 5) == 2
    assert get_count_prime_factors(100) == 4
    assert get_count_prime_factors(3301) == 1
    assert get_count_prime_factors(7775460) == 10


def test_k_primes_step():
    assert k_primes_step(10, 8, 2425364, 2425700) == []
    assert k_primes_step(6, 8, 2627371, 2627581) == [
        [2627408, 2627416], [2627440, 2627448], [2627496, 2627504]
    ]

"""Kata url: https://www.codewars.com/kata/55f347cfb44b879e1e00000d."""


def get_prime_factors(n, target):
    result = []
    for i in target:
        while not n % i:
            result.append(i)
            n //= i

    if n > 1:
        result.append(n)

    return result


def highest_bi_primefac(p1, p2, n):
    target = {p1, p2}

    for i in range(n, -1, -1):
        if i % p1:
            continue

        if i % p2:
            continue

        pf = get_prime_factors(i, target)

        if len(set(pf)) > 2:
            continue

        return [i, pf.count(p1), pf.count(p2)]


def test_highest_bi_primefac():
    assert highest_bi_primefac(2, 3, 50) == [48, 4, 1]
    assert highest_bi_primefac(5, 11, 1000) == [605, 1, 2]
    assert highest_bi_primefac(3, 13, 5000) == [4563, 3, 2]
    assert highest_bi_primefac(5, 7, 5000) == [4375, 4, 1]

"""Kata url: https://www.codewars.com/kata/6357205000fba205ed189a52."""


def magic():
    """https://bellard.org/pi."""
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while True:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1:
            yield int(d)
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1


def gen_pi():
    digits = magic()
    computed = 0
    cache = []

    def wrapper(n):
        nonlocal computed

        while (n + 1) > computed:
            cache.append(next(digits))
            computed += 1

        return cache[n]

    return wrapper


pi = gen_pi()


def test_pi():
    assert pi(0) == 3
    assert pi(1) == 1
    assert pi(2) == 4
    assert pi(10) == 5

    assert pi(100) == 9
    assert pi(500) == 2
    assert pi(1000) == 9

    assert pi(1001) == 3
    assert pi(5000) == 1
    assert pi(9999) == 7

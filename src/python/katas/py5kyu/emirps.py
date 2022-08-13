"""Kata url: https://www.codewars.com/kata/55de8eabd9bef5205e0000ba."""
import math


def is_prime_sup(k):
    return k % 2 and all(
        k % i
        for i in range(3, int(math.sqrt(k)) + 1, 2)
    )


def next_prime(i):
    while True:
        if is_prime_sup(i - 1):
            yield i - 1

        if is_prime_sup(i + 1):
            yield i + 1

        i += 6


def memoized(func):
    cache = set()
    covered = 0
    i = 18

    def inner(n):
        nonlocal covered, i, cache

        if n > covered:
            vals, p, r = func(n, cache, i)
            cache.update(vals)

            i = p - (p % 6)
            covered = n
            return r

        cached = [x for x in cache if x < n]
        return [len(cached), max(cached), sum(cached)]

    return inner


@memoized
def find_emirp(n, emirps, i=18):
    p = 13
    prime = next_prime(i)

    while p < n:
        emirp = int(str(p)[::-1])
        if emirp != p and is_prime_sup(emirp):
            emirps.add(p)

        p = next(prime)

    if not emirps:
        return emirps, p, [0, 0, 0]

    return emirps, p, [len(emirps), max(emirps), sum(emirps)]


def test_find_emirp():
    assert find_emirp(50) == [4, 37, 98]
    assert find_emirp(100) == [8, 97, 418]
    assert find_emirp(200) == [15, 199, 1489]
    assert find_emirp(500) == [20, 389, 3232]
    assert find_emirp(750) == [25, 743, 6857]
    assert find_emirp(1000) == [36, 991, 16788]
    assert find_emirp(3000) == [96, 1979, 103268]
    assert find_emirp(7000) == [147, 3929, 278175]
    assert find_emirp(10000) == [240, 9967, 1076242]
    assert find_emirp(15000) == [446, 14957, 3661772]
    assert find_emirp(20000) == [627, 19973, 6827225]
    assert find_emirp(50000) == [980, 39989, 19183366]
    assert find_emirp(75000) == [1135, 74959, 30404879]
    assert find_emirp(100000) == [1646, 99989, 76002998]

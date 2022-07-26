"""Kata url: https://www.codewars.com/kata/5539fecef69c483c5a000015."""

from math import sqrt
from typing import List


def is_not_pal_prime(n) -> bool:
    if n == 3:
        return False

    if not n % 2:
        return False

    if str(n) == str(n)[::-1]:
        return False

    return all(n % d for d in range(3, int(sqrt(n)) + 1, 2))


def backwards_prime(start: int, stop: int) -> List[int]:
    if not start % 2:
        start += 1

    return [
        i
        for i in range(start, stop + 1, 2)
        if is_not_pal_prime(i) and is_not_pal_prime(int(str(i)[::-1]))
    ]


def test_backward_prime():
    assert backwards_prime(1, 97) == [13, 17, 31, 37, 71, 73, 79, 97]
    assert backwards_prime(7000, 7100) == [7027, 7043, 7057]
    assert backwards_prime(400, 503) == []


def test_not_pal_prime():
    pal_primes = [2, 3, 5, 7, 11, 101, 131, 151, 181, 191]
    primes = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        137,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
        193,
        197,
        199,
        211,
        223,
        227,
        229,
        233,
        239,
        241,
        251,
        257,
        263,
        269,
        271,
        277,
        281,
        283,
        293,
    ]

    for i in range(300):
        if i in primes:
            assert is_not_pal_prime(i) == (i not in pal_primes)
        else:
            assert not is_not_pal_prime(i)

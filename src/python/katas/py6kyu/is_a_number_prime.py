"""Kata url: https://www.codewars.com/kata/5262119038c0985a5b00029f."""

from math import sqrt


def is_prime(num):
    if num < 3:
        return num == 2

    return num % 2 and all(
        num % n
        for n in range(3, int(sqrt(num) + 1), 2)
    )


def test_is_prime():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(73)
    assert not is_prime(75)
    assert not is_prime(-1)

    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(41)
    assert is_prime(5099)

    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(45)
    assert not is_prime(-5)
    assert not is_prime(-8)
    assert not is_prime(-41)

"""Kata url: https://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd."""


def my_gcd(x, y):
    return my_gcd(y, x % y) if y else x


def test_my_gcd():
    assert my_gcd(1, 3) == 1
    assert my_gcd(60, 12) == 12
    assert my_gcd(2672, 5678) == 334
    assert my_gcd(10927782, 6902514) == 846
    assert my_gcd(1590771464, 1590771620) == 4

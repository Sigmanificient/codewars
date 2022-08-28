"""Kata url: https://www.codewars.com/kata/52b5247074ea613a09000164."""
from math import ceil


def cooking_time(eggs):
    return ceil(eggs / 8) * 5


def test_cooking_time():
    assert cooking_time(0) == 0
    assert cooking_time(1) == 5
    assert cooking_time(5) == 5
    assert cooking_time(8) == 5
    assert cooking_time(9) == 10
    assert cooking_time(10) == 10
    assert cooking_time(16) == 10
    assert cooking_time(20) == 15
    assert cooking_time(100) == 65

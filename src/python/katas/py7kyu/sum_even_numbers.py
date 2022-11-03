"""Kata url: https://www.codewars.com/kata/586beb5ba44cfc44ed0006c3."""


def sum_even_numbers(seq):
    return sum(x for x in seq if not x % 2)


def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
    assert sum_even_numbers([]) == 0

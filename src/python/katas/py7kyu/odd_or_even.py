"""Kata url: https://www.codewars.com/kata/5949481f86420f59480000e7."""
from typing import List


def odd_or_even(arr: List[int]) -> str:
    return "odd" if sum(arr) % 2 else "even"


def test_odd_or_even():
    assert odd_or_even([0, 1, 2]) == "odd"
    assert odd_or_even([0, 1, 3]) == "even"
    assert odd_or_even([1023, 1, 2]) == "even"

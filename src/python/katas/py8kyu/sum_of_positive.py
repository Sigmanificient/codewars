"""Kata url: https://www.codewars.com/kata/5715eaedb436cf5606000381."""

from typing import List


def positive_sum(arr: List[int]) -> int:
    return sum(x for x in arr if x > 0)


def test_positive_sum():
    assert positive_sum([1, 2, 3, 4, 5]) == 15
    assert positive_sum([1, -2, 3, 4, 5]) == 13
    assert positive_sum([-1, 2, 3, 4, -5]) == 9

    assert positive_sum([]) == 0
    assert positive_sum([-1, -2, -3, -4, -5]) == 0

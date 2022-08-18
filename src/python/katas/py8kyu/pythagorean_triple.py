"""Kata url: https://www.codewars.com/kata/5951d30ce99cf2467e000013."""
from typing import List


def pythagorean_triple(integers: List[int]) -> int:
    a, b, c = sorted(integers)
    return (a ** 2 + b ** 2) == c ** 2


def test_pythagorean_triple():
    assert pythagorean_triple([3, 4, 5])
    assert not pythagorean_triple([3, 5, 9])

    assert pythagorean_triple([10, 8, 6])
    assert not pythagorean_triple([6, 12, 10])

    assert pythagorean_triple([12, 5, 13])
    assert not pythagorean_triple([5, 17, 13])

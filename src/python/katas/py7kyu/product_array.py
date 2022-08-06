"""Kata url: https://www.codewars.com/kata/5a905c2157c562994900009d."""
from typing import List


def product_array(numbers: List[int]) -> List[int]:
    p = 1
    for n in numbers:
        p *= n

    return [p // n for n in numbers]


def test_product_array():
    assert product_array([12, 20]) == [20, 12]
    assert product_array([12, 20]) == [20, 12]
    assert product_array([3, 27, 4, 2]) == [216, 24, 162, 324]
    assert product_array([13, 10, 5, 2, 9]) == [900, 1170, 2340, 5850, 1300]
    assert product_array([16, 17, 4, 3, 5, 2]) == [
        2040, 1920, 8160, 10880, 6528, 16320
    ]

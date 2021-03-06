"""Kata url: https://www.codewars.com/kata/511f11d355fe575d2c000001."""
from typing import List


def two_oldest_ages(ages: List[int]) -> List[int]:
    return sorted(ages)[-2:]


def test_two_oldest_ages():
    assert two_oldest_ages([1, 5, 87, 45, 8, 8]) == [45, 87]
    assert two_oldest_ages([6, 5, 83, 5, 3, 18]) == [18, 83]
    assert two_oldest_ages([10, 1]) == [1, 10]

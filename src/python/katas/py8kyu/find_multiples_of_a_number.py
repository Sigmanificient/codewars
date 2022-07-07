"""Kata url: https://www.codewars.com/kata/58ca658cc0d6401f2700045f."""
from typing import List


def find_multiples(integer: int, limit: int) -> List[int]:
    return [integer + integer * c for c in range(limit // integer)]


def test_find_multiples():
    assert find_multiples(1, 0) == []
    assert find_multiples(1, 1) == [1]
    assert find_multiples(5, 25) == [5, 10, 15, 20, 25]
    assert find_multiples(1, 2) == [1, 2]

"""Kata url: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d."""
from typing import List


def sort_array(arr: List[int]) -> List[int]:
    odds = sorted((v for v in arr if v % 2), reverse=True)
    return [odds.pop() if x % 2 else x for x in arr]


def test_sort_the_odd():
    assert sort_array([]) == []
    assert sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5 == 4]
    assert sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8 == 0]

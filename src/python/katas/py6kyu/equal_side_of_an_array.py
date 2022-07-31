"""Kata url: https://www.codewars.com/kata/5679aa472b8f57fb8c000047."""
from typing import List


def find_even_index(arr: List[int]) -> int:
    return next((i for i in range(len(arr)) if sum(arr[:i]) == sum(arr[i + 1 :])), -1)


def test_find_even_index():
    assert find_even_index([1, 2, 3, 4, 3, 2, 1]) == 3
    assert find_even_index([1, 100, 50, -51, 1, 1]) == 1
    assert find_even_index([1, 2, 3, 4, 5, 6]) == -1
    assert find_even_index([20, 10, 30, 10, 10, 15, 35]) == 3
    assert find_even_index([20, 10, -80, 10, 10, 15, 35]) == 0
    assert find_even_index([10, -80, 10, 10, 15, 35, 20]) == 6
    assert find_even_index(list(range(1, 100))) == -1
    assert find_even_index([0, 0, 0, 0, 0]) == 0
    assert find_even_index([-1, -2, -3, -4, -3, -2, -1]) == 3
    assert find_even_index(list(range(-100, -1))) == -1

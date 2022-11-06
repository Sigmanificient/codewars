"""Kata url: https://www.codewars.com/kata/554dc2b88fbafd2e95000125."""
import math


def vector_length(vector):
    (x_a, y_a), (x_b, y_b) = vector
    return math.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)


def test_vector_length():
    assert vector_length([[0, 1], [0, 0]]) == 1
    assert vector_length([[0, 3], [4, 0]]) == 5
    assert vector_length([[1, -1], [1, -1]]) == 0

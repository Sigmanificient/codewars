"""Kata url: https://www.codewars.com/kata/5648b12ce68d9daa6b000099."""
from typing import List


def number(bus_stops: List[int]) -> int:
    a, b = zip(*bus_stops)
    return sum(a) - sum(b)


def test_number():
    assert number([[10, 0], [3, 5], [5, 8]]) == 5
    assert number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]) == 17
    assert number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]) == 21

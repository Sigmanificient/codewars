"""Kata url: https://www.codewars.com/kata/5715eaedb436cf5606000381."""

from typing import List


def positive_sum(arr: List[int]) -> int:
    return sum(x for x in arr if x > 0)

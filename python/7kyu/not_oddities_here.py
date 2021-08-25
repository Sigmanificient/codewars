"""Kata url: https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce."""

from typing import List


def no_odds(values: List[int]) -> List[int]:
    return [x for x in values if not x % 2]
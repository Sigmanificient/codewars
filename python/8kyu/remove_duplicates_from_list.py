"""Kata url: https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118."""

from typing import List


def distinct(seq: List[int]) -> List[int]:
    return sorted(list(set(seq)), key=lambda x: seq.index(x))

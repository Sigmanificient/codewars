"""Kata url: https://www.codewars.com/kata/57cfdf34902f6ba3d300001e."""

from typing import List


def two_sort(array: List[str]) -> str:
    return '***'.join(sorted(array)[0])

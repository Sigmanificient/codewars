"""Kata url: https://www.codewars.com/kata/56e2f59fb2ed128081001328."""

from typing import List


def print_array(arr: List[int]) -> str:
    return ','.join(map(str, arr))

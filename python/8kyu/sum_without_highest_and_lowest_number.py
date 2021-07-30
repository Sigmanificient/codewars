"""Kata url: https://www.codewars.com/kata/576b93db1129fcf2200001e6."""

from typing import Optional, List


def sum_array(arr: Optional[List[int]]) -> int:
    return sum(sorted(arr)[1:-1]) if arr else 0

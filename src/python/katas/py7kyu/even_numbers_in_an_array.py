"""Kata url: https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c."""

from typing import List


def even_numbers(arr: List[int], n: int) -> List[int]:
    odds: List[int] = [x for x in arr if not x % 2]
    return odds[len(odds) - n:]

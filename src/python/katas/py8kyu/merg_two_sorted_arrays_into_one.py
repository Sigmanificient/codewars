"""Kata url: https://www.codewars.com/kata/5899642f6e1b25935d000161."""


from typing import List


def merge_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    return sorted(set(arr1 + arr2))

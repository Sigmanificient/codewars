"""Kata url: https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c."""
from typing import List


def max_sequence(arr: List[int]) -> List[int]:
    if not arr:
        return 0

    sub_max = sum(arr)

    for i in range(len(arr)):
        off_max = len(arr) - i

        for j in range(0, off_max + 1):
            s = sum(arr[i: i + j])
            if s > sub_max:
                sub_max = s

    return sub_max

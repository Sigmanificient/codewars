"""Kata url: https://www.codewars.com/kata/57eaeb9578748ff92a000009."""

from typing import List, Union


def sum_mix(arr: List[Union[int, str]]) -> int:
    return sum(map(int, arr))

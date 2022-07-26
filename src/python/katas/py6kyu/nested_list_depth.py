"""Kata url: https://www.codewars.com/kata/56b3b9c7a6df24cf8c00000e."""
from typing import List, Union


RecursiveList = List[Union[bool, str, int, "RecursiveList"]]


def list_depth(lst: RecursiveList, d: int = 0) -> int:
    if not isinstance(lst, list):
        return d

    return max(list_depth(item, d + 1) for item in lst) if lst else d + 1

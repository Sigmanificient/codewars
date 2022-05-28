"""Kata url: https://www.codewars.com/kata/54e6533c92449cc251001667."""

from typing import List, Optional


def unique_in_order(iterable: str) -> List[str]:
    last: Optional[str] = None
    array: List[str] = []
    for element in iterable:
        if last == element:
            continue
        array.append(element)
        last: Optional[str] = element
    return array

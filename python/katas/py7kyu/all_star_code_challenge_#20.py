"""Kata url: https://www.codewars.com/kata/5865a75da5f19147370000c7."""
from typing import List, Union


def add_arrays(
    array: List[Union[int, str]], array2: List[Union[int, str]]
) -> List[Union[int, str]]:
    if len(array) != len(array2):
        raise ValueError

    return [a + b for a, b in zip(array, array2)]

from typing import List, Union


def add_arrays(array1: List[Union[int, str]], array2: List[Union[int, str]]) -> List[Union[int, str]]:
    """Kata url: https://www.codewars.com/kata/5865a75da5f19147370000c7."""
    if len(array1) != len(array2):
        raise ValueError

    return [a + b for a, b in zip(array1, array2)]

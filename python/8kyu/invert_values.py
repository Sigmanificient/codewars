from typing import List


def invert(lst: List[int]) -> List[int]:
    """Kata url: https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad."""
    return [-x for x in lst]

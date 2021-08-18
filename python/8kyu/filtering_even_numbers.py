"""Kata url: https://www.codewars.com/kata/566dc566f6ea9a14b500007b."""

from typing import List


def kata_13_december(lst: List[int]) -> List[int]:
    return [x for x in lst if x % 2]

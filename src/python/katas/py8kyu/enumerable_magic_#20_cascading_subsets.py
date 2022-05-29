"""Kata url: https://www.codewars.com/kata/545af3d185166a3dec001190."""

from typing import List


def each_cons(lst: List[int], n: int) -> List[List[int]]:
    return [lst[i: i + n] for i in range(len(lst) - n + 1)]

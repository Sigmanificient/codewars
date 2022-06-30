"""Kata url: https://www.codewars.com/kata/545af3d185166a3dec001190."""

from typing import List


def each_cons(lst: List[int], n: int) -> List[List[int]]:
    return [lst[i: i + n] for i in range(len(lst) - n + 1)]


def test_each():
    assert each_cons([], 3) == []
    assert each_cons([3, 5, 8, 13], 1) == [[3], [5], [8], [13]]
    assert each_cons([3, 5, 8, 13], 2) == [[3, 5], [5, 8], [8, 13]]
    assert each_cons([3, 5, 8, 13], 3) == [[3, 5, 8], [5, 8, 13]]

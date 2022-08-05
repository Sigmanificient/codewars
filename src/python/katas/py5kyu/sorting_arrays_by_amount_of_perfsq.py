"""Kata url: https://www.codewars.com/kata/582fdcc039f654905400001e."""
from collections import defaultdict
from math import sqrt
from itertools import permutations
from typing import List, DefaultDict, Dict, Callable


def memoized(func: Callable[[int], int]) -> Callable[[int], int]:
    cache: Dict[int, int] = {}

    def inner(k: int) -> int:
        if k in cache:
            return cache[k]

        r: int = func(k)
        cache[k] = r
        return r

    return inner


@memoized
def find_perfsq_count(k: int) -> int:
    str_num = str(k)
    return sum(
        not sqrt(int(''.join(variant))) % 1
        for variant in set(permutations(str_num))
    )


def sort_by_perfsq(arr: List[int]) -> List[int]:
    squares: DefaultDict[int, List[int]] = defaultdict(list)

    for num in arr:
        squares[find_perfsq_count(num)].append(num)

    sorted_arr: List[int] = []
    for key in sorted(squares.keys(), reverse=True):
        sorted_arr.extend(sorted(squares[key]))

    return sorted_arr


def test_sort_by_perfsq():
    assert sort_by_perfsq(
        [715, 112, 136, 169, 144]
    ) == [169, 144, 112, 136, 715]

    assert sort_by_perfsq(
        [234, 61, 16, 441, 144, 728]
    ) == [144, 441, 16, 61, 234, 728]

    assert sort_by_perfsq(
        [4468, 446689, 169, 4477, 1345689]
    ) == [1345689, 169, 4468, 4477, 446689]

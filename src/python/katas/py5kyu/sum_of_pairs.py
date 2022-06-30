"""Kata url: https://www.codewars.com/kata/54d81488b981293527000c8f."""

from collections import defaultdict
from typing import Optional, List, DefaultDict


def sum_pairs(ints: List[int], s: int) -> Optional[List[int]]:
    occ: DefaultDict[int, int] = defaultdict(int)
    o_ints = []

    for i in ints:  # eliminate occurrences above 2 times
        occ[i] += 1
        if occ[i] <= 2:
            o_ints.append(i)

    ol = len(o_ints)
    for off in range(1, ol):
        for c, i in enumerate(o_ints[:-off]):
            if i + (j := o_ints[c + off]) == s:
                return [i, j]

    return None


def test_sum_pairs():
    assert sum_pairs([1, 4, 8, 7, 3, 15], 8) == [1, 7]
    assert sum_pairs([1, -2, 3, 0, -6, 1], -6) == [0, -6]
    assert sum_pairs([20, -13, 40], -7) is None
    assert sum_pairs([1, 2, 3, 4, 1, 0], 2) == [1, 1]
    assert sum_pairs([10, 5, 2, 3, 7, 5], 10) == [3, 7]
    assert sum_pairs([4, -2, 3, 3, 4], 8) == [4, 4]
    assert sum_pairs([0, 2, 0], 0) == [0, 0]
    assert sum_pairs([5, 9, 13, -3], 10) == [13, -3]

    from time import perf_counter

    marker = perf_counter()
    assert sum_pairs([13] + ([1] * 999999) + [-3], 10) == [13, -3]
    assert (perf_counter() - marker) < 1

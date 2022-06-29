"""Kata: https://www.codewars.com/kata/554ca54ffa7d91b236000023."""
from collections import defaultdict
from typing import List, DefaultDict


def delete_nth(order: List[int], max_e: int) -> List[int]:
    tracker: DefaultDict[int, int] = defaultdict(int)
    r = []

    for i in order:
        tracker[i] += 1
        if tracker[i] <= max_e:
            r.append(i)

    return r


def test_delete_nth():
    assert delete_nth([20, 37, 20, 21], 1) == [20, 37, 21]
    assert delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]

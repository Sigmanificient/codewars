"""Kata url: https://www.codewars.com/kata/5694d22eb15d78fe8d00003a."""

from collections import defaultdict
from typing import Optional, List, DefaultDict


def group_in_10s(*args: int) -> List[Optional[List[int]]]:
    if not args:
        return []

    groups: DefaultDict[int, List[int]] = defaultdict(list)

    for a in sorted(args):
        groups[a // 10].append(a)

    return [groups.get(x) for x in range((max(args) // 10) + 1)]


def test_group_in_10s():
    assert group_in_10s() == []
    assert group_in_10s(1, 2, 3) == [[1, 2, 3]]
    assert group_in_10s(100) == [None] * 10 + [[100]]

    assert group_in_10s(8, 12, 38, 3, 17, 19, 25, 35, 50) == [
        [3, 8], [12, 17, 19], [25], [35, 38], None, [50]
    ]

    assert group_in_10s(12, 10, 11, 13, 25, 28, 29, 49, 51, 90) == [
        None, [10, 11, 12, 13], [25, 28, 29], None,
        [49], [51], None, None, None, [90]
    ]

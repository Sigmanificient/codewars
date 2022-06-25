"""Kata url: https://www.codewars.com/kata/5526fc09a1bbd946250002dc."""
from typing import List


def find_outlier(integers: List[int]) -> int:
    odds = [x % 2 for x in integers]
    return integers[odds.index(sorted(odds, key=odds.count)[0])]


def test_find_outlier():
    assert find_outlier([2, 4, 6, 8, 10, 3]) == 3
    assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11
    assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160

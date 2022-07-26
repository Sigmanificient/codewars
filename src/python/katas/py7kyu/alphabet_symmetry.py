"""Kata url: https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0."""

from string import ascii_lowercase
from typing import List


def solve(arr: List[str]) -> List[str]:
    return [
        sum(ascii_lowercase.index(i) == c for c, i in enumerate(item.lower()))
        for item in arr
    ]


def test_solve():
    assert solve(["abode", "ABc", "xyzD"]) == [4, 3, 1]
    assert solve(["abide", "ABc", "xyz"]) == [4, 3, 0]
    assert solve(["IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc"]) == [6, 5, 7]
    assert solve(["encode", "abc", "xyzD", "ABmD"]) == [1, 3, 1, 3]

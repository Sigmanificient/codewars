"""Kata url: https://www.codewars.com/kata/5ce399e0047a45001c853c2b."""
from typing import List


def parts_sums(ls: List[int]) -> List[int]:
    n = sum(ls)
    out = [n]

    for i in ls:
        n -= i
        out.append(n)

    return out


def test_parts_sums():
    assert parts_sums([]) == [0]
    assert parts_sums([0, 1, 3, 6, 10]) == [20, 20, 19, 16, 10, 0]
    assert parts_sums([1, 2, 3, 4, 5, 6]) == [21, 20, 18, 15, 11, 6, 0]

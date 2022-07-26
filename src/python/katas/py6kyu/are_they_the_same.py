"""Kata url: https://www.codewars.com/kata/550498447451fbbd7600041c."""

from typing import List, Optional


def comp(array: Optional[List[int]], array2: Optional[List[int]]) -> bool:
    if array is None or array2 is None:
        return False

    if len(array) != len(array2):
        return False

    return all(i * i == j for i, j in zip(sorted(array, key=abs), sorted(array2)))


def test_comp():
    assert not comp(None, [1, 2, 3])
    assert not comp([1, 2, 3], None)

    assert not comp([1, 2, 3], [1, 2, 3, 4])

    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [
        11 * 11,
        121 * 121,
        144 * 144,
        19 * 19,
        161 * 161,
        19 * 19,
        144 * 144,
        19 * 19,
    ]
    assert comp(a1, a2)

    a2 = [
        11 * 21,
        121 * 121,
        144 * 144,
        19 * 19,
        161 * 161,
        19 * 19,
        144 * 144,
        19 * 19,
    ]
    assert not comp(a1, a2)

    a2 = [
        11 * 11,
        121 * 121,
        144 * 144,
        190 * 190,
        161 * 161,
        19 * 19,
        144 * 144,
        19 * 19,
    ]
    assert not comp(a1, a2)

"""Kata url: https://www.codewars.com/kata/5a34b80155519e1a00000009."""

from typing import List


def multiple_of_index(arr: List[int]) -> List[int]:
    return [x for c, x in enumerate(arr[1::]) if not (x / (c + 1)) % 1]


def test_multiple_of_index():
    assert multiple_of_index([22, -6, 32, 82, 9, 25]) == [-6, 32, 25]
    assert multiple_of_index([68, -1, 1, -7, 10, 10]) == [-1, 10]
    assert multiple_of_index([11, -11]) == [-11]
    assert multiple_of_index([-56, -85, 72, -26, -14, 76, -27, 72, 35, -21, -67, 87, 0, 21, 59, 27, -92, 68]) == [-85, 72, 0, 68]
    assert multiple_of_index([28, 38, -44, -99, -13, -54, 77, -51]) == [38, -44, -99]
    assert multiple_of_index([-1, -49, -1, 67, 8, -60, 39, 35]) == [-49, 8, -60, 35]

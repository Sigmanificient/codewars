"""Kata url: https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036."""

from typing import List


def to_csv_text(array: List[List[int]]) -> str:
    return '\n'.join(
        ','.join(str(item) for item in line) for line in array
    )


def test_to_csv_text():
    assert to_csv_text(
        [
            [0, 1, 2, 3, 45],
            [10, 11, 12, 13, 14],
            [20, 21, 22, 23, 24],
            [30, 31, 32, 33, 34]
        ]
    ) == "0,1,2,3,45\n10,11,12,13,14\n20,21,22,23,24\n30,31,32,33,34"

    assert to_csv_text(
        [
            [-25, 21, 2, -33, 48],
            [30, 31, -32, 33, -34]
        ]
    ) == "-25,21,2,-33,48\n30,31,-32,33,-34"

    assert to_csv_text(
        [
            [5, 55, 5, 5, 55],
            [6, 6, 66, 23, 24],
            [666, 31, 66, 33, 7]
        ]
    ) == "5,55,5,5,55\n6,6,66,23,24\n666,31,66,33,7"

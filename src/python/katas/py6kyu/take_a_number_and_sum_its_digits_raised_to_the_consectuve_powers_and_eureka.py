"""Kata url: https://www.codewars.com/kata/5626b561280a42ecc50000d1."""

from typing import List


def sum_dig_pow(a: int, b: int) -> List[int]:
    return [
        x
        for x in range(a, b + 1)
        if sum(int(d) ** c for c, d in enumerate(str(x), start=1)) == x
    ]


def test_sum_dig_pow():
    assert sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
    assert sum_dig_pow(10, 89) == [89]
    assert sum_dig_pow(10, 100) == [89]
    assert sum_dig_pow(90, 100) == []
    assert sum_dig_pow(89, 135) == [89, 135]
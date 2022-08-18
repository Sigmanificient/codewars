"""Kata url: https://www.codewars.com/kata/622de76d28bf330057cd6af8."""
from typing import List

digits: List[int] = [9, 180, 2700, 36000, 450000, 5400000]


def amount_of_pages(summary: int) -> int:
    i = t = 0

    while summary >= digits[i]:
        summary -= digits[i]
        t += digits[i] / (i + 1)
        i += 1

    return summary / (i + 1) + t


def test_amount_of_pages():
    assert amount_of_pages(5) == 5
    assert amount_of_pages(25) == 17
    assert amount_of_pages(1095) == 401
    assert amount_of_pages(185) == 97
    assert amount_of_pages(660) == 256

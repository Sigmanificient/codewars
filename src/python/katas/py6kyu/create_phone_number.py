"""Kata url: https://www.codewars.com/kata/525f50e3b73515a6db000b83."""

from typing import List


def create_phone_number(n: List[int]) -> str:
    sn = "".join(map(str, n))
    return f"({sn[:3]}) {sn[3:6]}-{sn[6:]}"


def test_create_phone_number():
    assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"
    assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"

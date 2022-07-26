"""Kata url: https://www.codewars.com/kata/57a083a57cb1f31db7000028."""

from typing import List


def powers_of_two(n: int) -> List[int]:
    return [2**i for i in range(n + 1)]


def test_powers_of_two():
    assert powers_of_two(0) == [1]
    assert powers_of_two(1) == [1, 2]
    assert powers_of_two(4) == [1, 2, 4, 8, 16]

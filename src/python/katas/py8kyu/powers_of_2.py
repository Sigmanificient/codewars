"""Kata url: https://www.codewars.com/kata/57a083a57cb1f31db7000028."""

from typing import List


def powers_of_two(n: int) -> List[int]:
    return [2 ** i for i in range(n + 1)]

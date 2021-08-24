# Kata url: https://www.codewars.com/kata/58ca658cc0d6401f2700045f.
from typing import List


def find_multiples(integer: int, limit: int) -> List[int]:
    return [integer + integer * c for c in range(limit // integer)]

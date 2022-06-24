"""Kata url: https://www.codewars.com/kata/56269eb78ad2e4ced1000013."""

import math


def find_next_square(sq: int) -> float:
    r: float = math.sqrt(sq)

    return -1 if r % 1 else (r + 1) ** 2


def test_find_next_square():
    assert find_next_square(121) == 144
    assert find_next_square(625) == 676
    assert find_next_square(319225) == 320356
    assert find_next_square(15241383936) == 15241630849

    assert find_next_square(342786627) == -1

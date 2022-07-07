"""Kata url: https://www.codewars.com/kata/55d1d6d5955ec6365400006d."""
import math


def round_to_next5(n: int) -> int:
    return math.ceil(n / 5) * 5


def test_round_to_next5():
    assert round_to_next5(0) == 0
    assert round_to_next5(1) == 5

    assert round_to_next5(-1) == 0

    assert round_to_next5(5) == 5
    assert round_to_next5(7) == 10

    assert round_to_next5(20) == 20
    assert round_to_next5(39) == 40

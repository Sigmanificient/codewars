"""Kata url: https://www.codewars.com/kata/526571aae218b8ee490006f4."""


def count_bits(n: int) -> int:
    return sum(i == '1' for i in f'{n:b}')


def test_count_bits():
    assert count_bits(0) == 0
    assert count_bits(4) == 1
    assert count_bits(7) == 3
    assert count_bits(9) == 2
    assert count_bits(10) == 2

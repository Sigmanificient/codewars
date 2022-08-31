"""Kata url: https://www.codewars.com/kata/58845748bd5733f1b300001f."""


def range_bit_count(a, b):
    return sum(
        f'{i:b}'.count('1')
        for i in range(a, b + 1)
    )


def test_range_bit_count():
    assert range_bit_count(2, 7) == 11
    assert range_bit_count(0, 1) == 1
    assert range_bit_count(4, 4) == 1

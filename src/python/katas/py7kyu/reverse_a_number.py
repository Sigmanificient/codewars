"""Kata url: https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5."""


def reverse_number(n):
    an = abs(n)
    sign = 2 * (n > 0) - 1
    return int(str(an)[::-1]) * sign


def test_reverse_number():
    assert reverse_number(123) ==  321
    assert reverse_number(-123) == -321
    assert reverse_number(1000) ==  1
    assert reverse_number(4321234) ==  4321234
    assert reverse_number(5) ==  5
    assert reverse_number(0) ==  0
    assert reverse_number(98989898) ==  89898989

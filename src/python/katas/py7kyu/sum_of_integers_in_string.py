"""Kata url: https://www.codewars.com/kata/598f76a44f613e0e0b000026."""
import re


def sum_of_integers_in_string(s):
    return sum(map(int, re.findall(r'\d+', s)))


def test_sum_of_integers_in_string():
    assert sum_of_integers_in_string("12.4") == 16
    assert sum_of_integers_in_string("h3ll0w0rld") == 3
    assert sum_of_integers_in_string("2 + 3 = ") == 5
    assert sum_of_integers_in_string(
        "Our company made approximately "
        "1 million in gross revenue last quarter."
    ) == 1
    assert sum_of_integers_in_string(
        "The Great Depression lasted "
        "from 1929 to 1939."
    ) == 3868
    assert sum_of_integers_in_string("Dogs are our best friends.") == 0
    assert sum_of_integers_in_string("C4t5 are 4m4z1ng.") == 18
    assert sum_of_integers_in_string(
        "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"
    ) == 3635

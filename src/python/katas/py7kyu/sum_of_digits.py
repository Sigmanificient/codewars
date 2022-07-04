"""Kata url: https://www.codewars.com/kata/59cf805aaeb28438fe00001c."""

from typing import Optional, Union


def sum_of_digits(digits: Optional[Union[int, str]]) -> str:
    if digits is None:
        return ''

    digits = str(digits)
    return ' + '.join(digits) + f" = {sum(map(int, digits))}"


def test_sum_of_digits():
    assert sum_of_digits("3433") == "3 + 4 + 3 + 3 = 13"
    assert sum_of_digits("64323") == "6 + 4 + 3 + 2 + 3 = 18"
    assert sum_of_digits("8") == "8 = 8"
    assert sum_of_digits(3433) == "3 + 4 + 3 + 3 = 13"
    assert sum_of_digits(64323) == "6 + 4 + 3 + 2 + 3 = 18"
    assert sum_of_digits(8) == "8 = 8"
    assert sum_of_digits(None) == ""

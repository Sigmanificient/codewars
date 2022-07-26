"""Kata url: https://www.codewars.com/kata/57eaec5608fed543d6000021."""

from typing import List, Union


def div_con(x: List[Union[int, str]]) -> int:
    s = sum(int(i) for i in x if isinstance(i, str))
    return sum(i for i in x if isinstance(i, int)) - s


def test_div_con():
    assert div_con([9, 3, "7", "3"]) == 2
    assert div_con(["5", "0", 9, 3, 2, 1, "9", 6, 7]) == 14
    assert div_con(["3", 6, 6, 0, "5", 8, 5, "6", 2, "0"]) == 13
    assert div_con(["1", "5", "8", 8, 9, 9, 2, "3"]) == 11
    assert div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]) == 61

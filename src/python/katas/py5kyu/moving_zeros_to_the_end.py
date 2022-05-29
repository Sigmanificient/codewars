"""Kata: https://www.codewars.com/kata/52597aa56021e91c93000cb0."""
from typing import List


def move_zeros(array: List[int]) -> List[int]:
    filtered: List[int] = list(filter(bool, array))
    return filtered + [0] * (len(array) - len(filtered))


def _li(string) -> List[int]:
    return list(map(int, string))


def test_li():
    assert _li('123') == [1, 2, 3]


def test_move_zeros():
    assert move_zeros(_li('1201010301')) == _li('1211310000')
    assert move_zeros(_li('90091201010301900009')) == _li('99121131990000000000')
    assert move_zeros(_li('00')) == _li('00')
    assert move_zeros(_li('0')) == _li('0')
    assert move_zeros([]) == []

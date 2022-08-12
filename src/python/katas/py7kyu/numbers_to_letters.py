"""Kata url: https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c."""
from string import ascii_lowercase
from typing import List

CHARSET = f'{ascii_lowercase[::-1]}!? '


def switcher(arr: List[int]) -> str:
    return ''.join(CHARSET[int(i) - 1] for i in arr)


def test_switcher():
    assert switcher(['24', '12', '23', '22', '4', '26', '9', '8']) == 'codewars'
    assert switcher(
        ['25', '7', '8', '4', '14', '23', '8', '25', '23', '29', '16', '16', '4']
    ) == 'btswmdsbd kkw'
    assert switcher(['4', '24']) == 'wc'
    assert switcher(['12']) == 'o'
    assert switcher(
        ['12', '28', '25', '21', '25', '7', '11', '22', '15']
    ) == 'o?bfbtpel'

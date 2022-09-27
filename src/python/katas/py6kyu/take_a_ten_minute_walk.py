"""Kata url: https://www.codewars.com/kata/54da539698b8a2ad76000228."""
from typing import Literal, List

Cardinals = Literal['n', 's', 'e', 'w']


def is_valid_walk(walk: List[Cardinals]) -> bool:
    if len(walk) != 10:
        return False

    deviation = [0, 0]
    for d in walk:
        deviation[d in 'ns'] += (d in 'se') or -1

    return all(d == 0 for d in deviation)


def test_is_valid_walk():
    assert is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])

    assert not is_valid_walk(['w'])
    assert not is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])
    assert not is_valid_walk(
        ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']
    )

"""Kata url: https://www.codewars.com/kata/58885a7bf06a3d466e0000e3."""
from collections import defaultdict


def pair_of_shoes(shoes):
    pairs = defaultdict(lambda: [0, 0])

    for typ_, size in shoes:
        pairs[size][typ_] += 1

    return all(
        left - right == 0
        for left, right in pairs.values()
    )


def test_pair_of_shoes():
    assert pair_of_shoes([[0, 21], [1, 23], [1, 21], [0, 23]])
    assert not pair_of_shoes([[0, 21], [1, 23], [1, 21], [1, 23]])
    assert pair_of_shoes([[0, 23], [1, 21], [1, 23], [0, 21], [1, 22], [0, 22]])
    assert pair_of_shoes([[0, 23], [1, 21], [1, 23], [0, 21]])
    assert not pair_of_shoes([[0, 23], [1, 21], [1, 22], [0, 21]])
    assert not pair_of_shoes([[0, 23]])
    assert pair_of_shoes([[0, 23], [1, 23]])
    assert pair_of_shoes([[0, 23], [1, 23], [1, 23], [0, 23]])
    assert not pair_of_shoes([[0, 23], [1, 22]])
    assert not pair_of_shoes([[0, 23], [1, 23], [1, 23], [0, 23], [0, 23], [0, 23]])

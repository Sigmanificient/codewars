"""Kata url: https://www.codewars.com/kata/5581e52ac76ffdea700000c1."""
from typing import Dict, List, Tuple

ALIVE: Dict[Tuple[int, int, int], int] = {
    (1, 1, 1): 0,
    (1, 1, 0): 0,
    (1, 0, 1): 0,
    (1, 0, 0): 1,
    (0, 1, 1): 1,
    (0, 1, 0): 1,
    (0, 0, 1): 1,
    (0, 0, 0): 0
}


def rule30(cells: List[int], n: int) -> List[int]:
    if not n:
        return cells

    cells = [0] * n + cells + [0] * n

    length = len(cells) - 1
    next_gen = []
    for _ in range(n):
        for c, up in enumerate(cells):
            up_left = cells[c - 1] if c else 0
            up_right = cells[c + 1] if c < length else 0

            next_gen.append(ALIVE[(up_left, up, up_right)])

        cells, next_gen = next_gen, []
    return cells


def test_rule_30():
    assert rule30([1], 1) == [1, 1, 1]
    assert rule30([1], 2) == [1, 1, 0, 0, 1]
    assert rule30([1], 21) == [
        1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1,
        0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1
    ]

    assert rule30([1, 0, 0, 0, 1, 1], 3) == [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1]
    assert rule30([1, 1, 1], 5) == [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1]

    assert rule30([0], 5) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert rule30([0], 0) == [0]
    assert rule30([1, 1, 1], 0) == [1, 1, 1]
    assert rule30([1, 0, 0, 0, 1, 1], 3) == [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1]
    assert rule30([0], 3) == [0, 0, 0, 0, 0, 0, 0]
    assert rule30([1, 0, 0, 0, 1, 1], 3) == [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1]
    assert rule30([1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1], 1) == [
        1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1
    ]

    assert rule30([1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1], 75) == [
        1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1,
        0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1,
        1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1,
        1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1,
        0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0,
        0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1
    ]

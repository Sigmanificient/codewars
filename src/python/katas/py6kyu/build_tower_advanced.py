"""Kata url: https://www.codewars.com/kata/57675f3dedc6f728ee000256."""
from typing import Tuple, List


def tower_builder(n_floors: int, block_size: Tuple[int, int]) -> List[str]:
    w, h = block_size
    cw = w

    out = []
    for _ in range(n_floors):
        block = ['*' * cw for _ in range(h)]
        out.extend(block)
        cw += 2 * w

    max_width = len(out[-1])
    return [l_out.center(max_width) for l_out in out]


def test_tower_builder():
    assert tower_builder(1, (1, 1)) == ['*']
    assert tower_builder(3, (4, 2)) == [
        '        ****        ',
        '        ****        ',
        '    ************    ',
        '    ************    ',
        '********************',
        '********************'
    ]

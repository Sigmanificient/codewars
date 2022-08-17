"""Kata url: https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111."""
from time import perf_counter

marker = perf_counter()
goto = {
    'BG': 'R',
    'RG': 'B',
    'BR': 'G',
    'GB': 'R',
    'GR': 'B',
    'RB': 'G'
}


def triangle(row: str) -> str:
    while len(row) != 1:
        row = ''.join(
            a if a == b else goto[a + b]
            for a, b in zip(row, row[1::])
        )

    return row


def test_triangle():
    assert triangle('GB') == 'R'
    assert triangle('RRR') == 'R'
    assert triangle('RGBG') == 'B'
    assert triangle('RBRGBRB') == 'G'
    assert triangle('RBRGBRBGGRRRBGBBBGG') == 'G'
    assert triangle('B') == 'B'

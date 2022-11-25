"""Kata url: https://www.codewars.com/kata/59dd2c38f703c4ae5e000014."""

import re


def solve(s):
    matches = re.findall(r'\d+', s)
    return max(map(int, matches)) if matches else -1


def test_solve():
    assert solve('gh12cdy695m1') == 695
    assert solve('2ti9iei7qhr5') == 9
    assert solve('vih61w8oohj5') == 61
    assert solve('f7g42g16hcu5') == 42
    assert solve('lu1j8qbbb85') == 85

"""Kata url: https://www.codewars.com/kata/62cecd4e5487c10028996e04."""

from typing import Tuple


def race_podium(blocks: int) -> Tuple[int, int, int]:
    if blocks == 7:
        return 2, 4, 1

    snd = int(blocks / 3 + 2/3)
    first = snd + 1
    return snd, first, blocks - snd - first


def test_race_podium():
    assert race_podium(11) == (4, 5, 2)
    assert race_podium(6) == (2, 3, 1)
    assert race_podium(10) == (4, 5, 1)
    assert race_podium(100000) == (33334, 33335, 33331)
    assert race_podium(7) == (2, 4, 1)
    assert race_podium(8) == (3, 4, 1)

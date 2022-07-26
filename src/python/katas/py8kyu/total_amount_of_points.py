"""Kata url: https://www.codewars.com/kata/5bb904724c47249b10000131."""


from typing import List


def points(games: List[str]) -> int:
    point: int = 0

    for match in games:
        y, x = match.split(":")

        if x == y:
            point += 1
            continue

        if x < y:
            point += 3

    return point


def test_points():
    assert (
        points(["1:0", "2:0", "3:0", "4:0", "2:1", "3:1", "4:1", "3:2", "4:2", "4:3"])
        == 30
    )
    assert (
        points(["1:1", "2:2", "3:3", "4:4", "2:2", "3:3", "4:4", "3:3", "4:4", "4:4"])
        == 10
    )
    assert (
        points(["0:1", "0:2", "0:3", "0:4", "1:2", "1:3", "1:4", "2:3", "2:4", "3:4"])
        == 0
    )
    assert (
        points(["1:0", "2:0", "3:0", "4:0", "2:1", "1:3", "1:4", "2:3", "2:4", "3:4"])
        == 15
    )
    assert (
        points(["1:0", "2:0", "3:0", "4:4", "2:2", "3:3", "1:4", "2:3", "2:4", "3:4"])
        == 12
    )

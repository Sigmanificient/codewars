"""Kata url: https://www.codewars.com/kata/550f22f4d758534c1100025a."""
from typing import Literal, List

Direction = Literal["NORTH", "SOUTH", "EAST", "WEST"]


def dir_reduction(arr: List[Direction]) -> List[Direction]:
    reduced = True
    while reduced:
        reduced = False

        out = []
        i = 1

        while i < len(arr):
            if arr[i][0] + arr[i - 1][0] in {'NS', 'SN', 'WE', 'EW'}:
                reduced = True
                i += 2
                continue

            out.append(arr[i - 1])
            i += 1

        if i == len(arr):
            out.append(arr[i - 1])

        arr = out
    return out


def test_find_reduction():
    assert dir_reduction(
        ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    ) == ['WEST']
    assert dir_reduction(
        [
            "NORTH", "SOUTH", "EAST", "WEST", "NORTH",
            "NORTH", "SOUTH", "NORTH", "WEST", "EAST"
        ]
    ), ['NORTH', 'NORTH']

    assert dir_reduction(
        ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]
    ), []

    assert dir_reduction(
        ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"]
    ) == ["NORTH"]

    assert dir_reduction(
        [
            "EAST", "EAST", "WEST", "NORTH",
            "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"
        ]
    ), ["EAST", "NORTH"]

    assert dir_reduction(
        [
            "NORTH", "EAST", "NORTH", "EAST", "WEST",
            "WEST", "EAST", "EAST", "WEST", "SOUTH"
        ]
    ) == ["NORTH", "EAST"]

    assert dir_reduction(
        ["NORTH", "WEST", "SOUTH", "EAST"]
    ) == ["NORTH", "WEST", "SOUTH", "EAST"]

    assert dir_reduction([
        'NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST',
        'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']
    ) == [
        'NORTH', 'NORTH', 'EAST', 'SOUTH',
        'EAST', 'EAST', 'SOUTH', 'SOUTH'
    ]

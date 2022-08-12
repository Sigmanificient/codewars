"""Kata url: https://www.codewars.com/kata/59778cb1b061e877c50000cc."""
from typing import List


def arr_adder(arr: List[List[str]]) -> str:
    return ' '.join(map(''.join, zip(*arr)))


def test_arr_adder():
    assert arr_adder(
        [
            ['J', 'L', 'L', 'M'],
            ['u', 'i', 'i', 'a'],
            ['s', 'v', 'f', 'n'],
            ['t', 'e', 'e', '']
        ]
    ) == "Just Live Life Man"

    assert arr_adder([
        ['T', 'M', 'i', 't', 'p', 'o', 't', 'c'],
        ['h', 'i', 's', 'h', 'o', 'f', 'h', 'e'],
        ['e', 't', '', 'e', 'w', '', 'e', 'l'],
        ['', 'o', '', '', 'e', '', '', 'l'],
        ['', 'c', '', '', 'r', '', '', ''],
        ['', 'h', '', '', 'h', '', '', ''],
        ['', 'o', '', '', 'o', '', '', ''],
        ['', 'n', '', '', 'u', '', '', ''],
        ['', 'd', '', '', 's', '', '', ''],
        ['', 'r', '', '', 'e', '', '', ''],
        ['', 'i', '', '', '', '', '', ''],
        ['', 'a', '', '', '', '', '', '']
    ]
    ) == "The Mitochondria is the powerhouse of the cell"

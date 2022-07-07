"""Kata url: https://www.codewars.com/kata/5839edaa6754d6fec10000a2."""
from typing import List


def find_missing_letter(chars: List[str]) -> str:
    charset = 'abcdefghijklmnopqrstuvwxyz'
    string = ''.join(chars)

    if string.isupper():
        charset = charset.upper()

    for a, b in zip(charset[charset.index(string[0]):], string):
        if a != b:
            return a

    raise ValueError('No missing letter found')


def test_find_missing_letter():
    assert find_missing_letter(['a', 'b', 'c', 'd', 'f']) == 'e'
    assert find_missing_letter(['A', 'B', 'C', 'D', 'F']) == 'E'

    assert find_missing_letter(['O', 'Q', 'R', 'S']) == 'P'
    assert find_missing_letter(['V', 'X', 'Y', 'Z']) == 'W'

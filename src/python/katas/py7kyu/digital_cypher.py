"""Kata url: https://www.codewars.com/kata/592e830e043b99888600002d."""
import itertools
from string import ascii_lowercase

ALPHABET = {v: k for (k, v) in enumerate(ascii_lowercase, start=1)}


def encode(message, key):
    key_cycle = itertools.cycle(map(int, str(key)))
    return [(ALPHABET[c] + next(key_cycle)) for c in message]


def test_encode():
    assert encode("scout", 1939) == [20, 12, 18, 30, 21]
    assert encode("masterpiece", 1939) == [
        14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8
    ]

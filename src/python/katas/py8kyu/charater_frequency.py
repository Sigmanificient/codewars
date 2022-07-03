"""Kata url: https://www.codewars.com/kata/548ef5b7f33a646ea50000b2."""
from typing import Dict


def char_freq(message: str) -> Dict[str, int]:
    return {
        char: message.count(char) for char in message
    }


def test_char_freq():
    assert char_freq("") == {}
    assert char_freq("I") == {'I': 1}
    assert char_freq("I like cats") == {
        'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1,
        'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1
    }

    assert char_freq("Hello World") == {
        ' ': 1, 'H': 1, 'W': 1, 'd': 1, 'e': 1, 'l': 3, 'o': 2, 'r': 1
    }

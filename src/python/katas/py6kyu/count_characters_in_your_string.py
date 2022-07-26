"""Kata url: https://www.codewars.com/kata/52efefcbcdf57161d4000091."""
from typing import Dict


def count(string) -> Dict[str, int]:
    return {i: string.count(i) for i in string}


def test_count():
    assert count("") == {}
    assert count("a") == {"a": 1}
    assert count("aba") == {"a": 2, "b": 1}
    assert count("aaabbb") == {"a": 3, "b": 3}
    assert count("aabbcc") == {"a": 2, "b": 2, "c": 2}
    assert count("aabbccddeefghi") == {
        "a": 2,
        "b": 2,
        "c": 2,
        "d": 2,
        "e": 2,
        "f": 1,
        "g": 1,
        "h": 1,
        "i": 1,
    }

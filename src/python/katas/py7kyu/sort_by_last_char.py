"""Kata url: https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0."""
from typing import List


def last(s: str) -> List[str]:
    return sorted(s.split(' '), key=lambda w: w[-1])


def test_last():
    assert last("man i need a taxi up to ubud") == [
        "a", "need", "ubud", "i", "taxi", "man", "to", "up"
    ]
    assert last("what time are we climbing up the volcano") == [
        "time", "are", "we", "the", "climbing", "volcano", "up", "what"
    ]

    assert last("take me to semynak") == ["take", "me", "semynak", "to"]
    assert last("massage yes massage yes massage") == [
        "massage", "massage", "massage", "yes", "yes"
    ]
    assert last("take bintang and a dance please") == [
        "a", "and", "take", "dance", "please", "bintang"
    ]

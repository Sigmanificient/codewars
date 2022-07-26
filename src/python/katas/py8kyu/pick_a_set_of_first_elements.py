"""Kata url: https://www.codewars.com/kata/572b77262bedd351e9000076."""


from typing import List


def first(seq: List[int], n: int = 1) -> List[int]:
    return seq[:n]


def test_first():
    seq = ["a", "b", "c", "d", "e"]
    assert first(seq) == ["a"]
    assert first(seq, 0) == []
    assert first(seq, 1) == ["a"]
    assert first(seq, 2) == ["a", "b"]
    assert first(seq, 10) == ["a", "b", "c", "d", "e"]

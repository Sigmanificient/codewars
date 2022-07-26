"""Kata url: https://www.codewars.com/kata/539ee3b6757843632d00026b."""

from typing import List


def capitals(word: str) -> List[int]:
    return [c for c, x in enumerate(word) if x.isupper()]


def test_capitals():
    assert capitals("codewars") == []
    assert capitals("CodEWaRs") == [0, 3, 4, 6]
    assert capitals("Hello, World") == [0, 7]

"""Kata url: https://www.codewars.com/kata/525c1a07bb6dda6944000031."""
from typing import List

websites: List[str] = ["codewars"] * 1000


def test_website():
    assert len(websites) == 1000
    assert isinstance(websites, list)
    assert list(set(websites)) == ["codewars"]
"""Kata url: https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd."""
from typing import List


def list_animals(animals: List[str]) -> str:
    return "\n".join(f"{c + 1}. {item}" for (c, item) in enumerate(animals)) + "\n"


def test_list_animals():
    assert list_animals(["cat"]) == "1. cat\n"
    assert list_animals(["dog", "cat", "elephant"]) == "1. dog\n2. cat\n3. elephant\n"
    assert list_animals(["cat", "elephant"]) == "1. cat\n2. elephant\n"
    assert (
        list_animals(["dog", "cat", "elephant", "mouse"])
        == "1. dog\n2. cat\n3. elephant\n4. mouse\n"
    )

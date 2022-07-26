"""Kata url: https://www.codewars.com/kata/5266876b8f4bf2da9b000362."""

from typing import List


def likes(names: List[str]) -> str:
    if not names:
        return "no one likes this"

    if len(names) == 1:
        return f"{names[0]} likes this"

    if len(names) < 4:
        return f'{", ".join(names[:-1])} and {names[-1]} like this'

    return f'{", ".join(names[:2])} and {len(names) - 2} others like this'


def test_likes():
    assert likes([]) == "no one likes this"
    assert likes(["Peter"]) == "Peter likes this"
    assert likes(["Jacob", "Alex"]) == "Jacob and Alex like this"
    assert likes(["Max", "John", "Mark"]) == "Max, John and Mark like this"
    assert (
        likes(["Alex", "Jacob", "Mark", "Max"]) == "Alex, Jacob and 2 others like this"
    )

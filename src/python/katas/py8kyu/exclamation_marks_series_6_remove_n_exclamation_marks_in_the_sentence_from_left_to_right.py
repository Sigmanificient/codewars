"""Kata url: https://www.codewars.com/kata/57faf7275c991027af000679."""
from typing import List


def remove(s: str, n: int) -> str:
    r: List[str] = []

    for char in s:
        if char == "!" and n:
            n -= 1
            continue

        r.append(char)
    return "".join(r)


def test_remove():
    assert remove("Hi!", 1) == "Hi"
    assert remove("Hi!!!", 1) == "Hi!!"

    assert remove("Hi!", 100) == "Hi"
    assert remove("Hi!!!", 1) == "Hi!!"
    assert remove("Hi!!!", 100) == "Hi"

    assert remove("!!!Hi !!hi!!! !hi", 1) == "!!Hi !!hi!!! !hi"
    assert remove("!!!Hi !!hi!!! !hi", 3) == "Hi !!hi!!! !hi"
    assert remove("!!!Hi !!hi!!! !hi", 5) == "Hi hi!!! !hi"
    assert remove("!!!Hi !!hi!!! !hi", 100) == "Hi hi hi"

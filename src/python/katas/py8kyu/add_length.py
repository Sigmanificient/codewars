"""Kata url: https://www.codewars.com/kata/559d2284b5bb6799e9000047."""

from typing import List


def add_length(str_: str) -> List[str]:
    return [f"{x} {len(x)}" for x in str_.split()]


def test_add_length():
    assert add_length('') == []
    assert add_length('y') == ["y 1"]
    assert add_length('you') == ["you 3"]
    assert add_length('apple ban') == ["apple 5", "ban 3"]
    assert add_length('you will win') == ["you 3", "will 4", "win 3"]

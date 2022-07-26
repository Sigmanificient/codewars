"""Kata url: https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9."""


def number(lines):
    return [f"{c}: {line}" for c, line in enumerate(lines, start=1)]


def test_numbers():
    assert number([]) == []
    assert number(["a", "b", "c"]) == ["1: a", "2: b", "3: c"]

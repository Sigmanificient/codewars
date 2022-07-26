"""Kata url: https://www.codewars.com/kata/5168bb5dfe9a00b126000018."""


def solution(string: str) -> str:
    return string[::-1]


def test_solution():
    assert solution("world") == "dlrow"
    assert solution("hello") == "olleh"
    assert solution("") == ""
    assert solution("h") == "h"

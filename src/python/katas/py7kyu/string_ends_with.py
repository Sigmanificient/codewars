"""Kata url: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d."""


def solution(string: str, ending: str) -> bool:
    return string.endswith(ending)


def test_solution():
    assert solution("abcde", "cde")
    assert not solution("abcde", "abc")
    assert solution("abcde", "")

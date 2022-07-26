"""Kata url: https://www.codewars.com/kata/50654ddff44f800200000007."""


def solution(a, b):
    if len(a) > len(b):
        a, b = b, a

    return f"{a}{b}{a}"


def test_solution():
    assert solution("45", "1") == "1451"
    assert solution("13", "200") == "1320013"
    assert solution("Soon", "Me") == "MeSoonMe"
    assert solution("U", "False") == "UFalseU"

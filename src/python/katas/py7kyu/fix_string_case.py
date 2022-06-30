"""Kata url: https://www.codewars.com/kata/5b180e9fedaa564a7000009a"""


def solve(s: str) -> str:
    low = sum(x.islower() for x in s)
    return s.upper() if len(s) > 2 * low else s.lower()


def test_solve():
    assert solve("code") == "code"
    assert solve("CODe") == "CODE"
    assert solve("COde") == "code"
    assert solve("Code") == "code"

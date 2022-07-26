"""Kata url: https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145."""


def hoop_count(n: int) -> str:
    return "Keep at it until you get it" if n < 10 else "Great, now move on to tricks"


def test_hoop_count():
    assert hoop_count(3) == "Keep at it until you get it"
    assert hoop_count(11) == "Great, now move on to tricks"

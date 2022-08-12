"""Kata url: https://www.codewars.com/kata/5aa736a455f906981800360d."""


def feast(beast: str, dish: str) -> bool:
    return (
        beast[0] == dish[0]
        and beast[-1] == dish[-1]
    )


def test_feast():
    assert feast("great blue heron", "garlic naan")
    assert feast("chickadee", "chocolate cake")
    assert not feast("brown bear", "bear claw")

"""Kata url: https://www.codewars.com/kata/56a946cd7bd95ccab2000055."""


def lowercase_count(string: str) -> int:
    return sum(x.islower() for x in string)

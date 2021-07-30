"""Kata url: https://www.codewars.com/kata/56f173a35b91399a05000cb7."""


def find_longest(string: str) -> int:
    return max(len(x) for x in string.split())

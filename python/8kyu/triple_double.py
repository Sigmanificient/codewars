"""Kata url: https://www.codewars.com/kata/5704aea738428f4d30000914."""


def triple_trouble(one: str, two: str, three: str) -> str:
    return ''.join(a + b + c for a, b, c in zip(one, two, three))

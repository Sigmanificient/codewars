"""Kata url: https://www.codewars.com/kata/55a8a36703fe4c45ed00005b."""


def multiple(x: int) -> str:
    return (
        "Bang" * (not x % 3)
        + "Boom" * (not x % 5)
        or "Miss"
    )

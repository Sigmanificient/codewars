"""Kata url: https://www.codewars.com/kata/5772da22b89313a4d50012f7."""


def greet(name: str, owner: str) -> str:
    return 'Hello {}'.format("boss" if name == owner else "guest")

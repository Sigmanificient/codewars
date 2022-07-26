"""Kata url: https://www.codewars.com/kata/5772da22b89313a4d50012f7."""


def greet(name: str, owner: str) -> str:
    return f'Hello {"boss" if name == owner else "guest"}'


def test_greet():
    assert greet("Daniel", "Daniel") == "Hello boss"
    assert greet("Greg", "Daniel") == "Hello guest"

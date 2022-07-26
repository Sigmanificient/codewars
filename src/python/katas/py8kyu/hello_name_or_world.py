"""Kata url: https://www.codewars.com/kata/57e3f79c9cb119374600046b."""


def hello(name: str = "") -> str:
    return f"Hello, {name.capitalize() if name else 'World'}!"


def test_hello():
    assert hello("John") == "Hello, John!"
    assert hello("aLIce") == "Hello, Alice!"
    assert hello("") == "Hello, World!"

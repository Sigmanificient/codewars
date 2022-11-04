"""Kata url: https://www.codewars.com/kata/55955a48a4e9c1a77500005a."""


def greet(name):
    return f"hello {name}!" if name else None


def test_greet():
    assert greet("Niks") == "hello Niks!"
    assert greet("Nick") == "hello Nick!"
    assert greet("") is None
    assert greet(None) is None

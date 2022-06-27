"""Kata url: https://www.codewars.com/kata/55225023e1be1ec8bc000390."""


def greet(name: str) -> str:
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"


def test_greet():
    assert greet("James") == "Hello, James!"
    assert greet("Jane") == "Hello, Jane!"
    assert greet("Jim") == "Hello, Jim!"
    assert greet("Johnny") == "Hello, my love!"

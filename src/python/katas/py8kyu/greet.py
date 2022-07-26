"""Kata url: https://www.codewars.com/kata/55a70521798b14d4750000a4."""


def greet(name) -> str:
    return f"Hello, {name} how are you doing today?"


def test_greet():
    assert greet("Ryan") == "Hello, Ryan how are you doing today?"
    assert greet("Shingles") == "Hello, Shingles how are you doing today?"

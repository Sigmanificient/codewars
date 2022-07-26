"""Kata url: https://www.codewars.com/kata/5302d846be2a9189af0001e4."""


from typing import List


def say_hello(name: List[str], city: str, state: str) -> str:
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"


def test_say_hello():
    assert (
        say_hello(["John", "Smith"], "Phoenix", "Arizona")
        == "Hello, John Smith! Welcome to Phoenix, Arizona!"
    )
    assert (
        say_hello(["Franklin", "Delano", "Roosevelt"], "Chicago", "Illinois")
        == "Hello, Franklin Delano Roosevelt! Welcome to Chicago, Illinois!"
    )
    assert (
        say_hello(["Wallace", "Russel", "Osbourne"], "Albany", "New York")
        == "Hello, Wallace Russel Osbourne! Welcome to Albany, New York!"
    )
    assert (
        say_hello(["Lupin", "the", "Third"], "Los Angeles", "California")
        == "Hello, Lupin the Third! Welcome to Los Angeles, California!"
    )
    assert (
        say_hello(["Marlo", "Stanfield"], "Baltimore", "Maryland")
        == "Hello, Marlo Stanfield! Welcome to Baltimore, Maryland!"
    )
    assert say_hello([], "", "") == "Hello, ! Welcome to , !"

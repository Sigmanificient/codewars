"""Kata url: https://www.codewars.com/kata/5625618b1fe21ab49f00001f."""


def say_hello(name: str) -> str:
    return f"Hello, {name}"


def test_say_hello():
    assert say_hello("Mr. Spock") == "Hello, Mr. Spock"
    assert say_hello("Captain Kirk") == "Hello, Captain Kirk"
    assert say_hello("Liutenant Uhura") == "Hello, Liutenant Uhura"
    assert say_hello("Dr. McCoy") == "Hello, Dr. McCoy"
    assert say_hello("Mr. Scott") == "Hello, Mr. Scott"

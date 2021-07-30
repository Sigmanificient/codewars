"""Kata url: https://www.codewars.com/kata/5302d846be2a9189af0001e4."""


from typing import List


def say_hello(name: List[str], city: str, state: str) -> str:
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"

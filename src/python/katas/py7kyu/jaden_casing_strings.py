"""Kata url: https://www.codewars.com/kata/5390bac347d09b7da40006f6."""


def to_jaden_case(string: str) -> str:
    return " ".join(w.capitalize() for w in string.split(" "))

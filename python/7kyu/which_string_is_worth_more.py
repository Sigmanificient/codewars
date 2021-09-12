"""Kata url: https://www.codewars.com/kata/5840586b5225616069000001."""


def highest_value(a: str, b: str) -> str:
    return a if sum(map(ord, a)) >= sum(map(ord, b)) else b

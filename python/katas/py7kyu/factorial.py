"""Kata url: https://www.codewars.com/kata/57a049e253ba33ac5e000212."""


def factorial(n: int) -> int:
    return n * factorial(n - 1) if n else 1

"""Kata url: https://www.codewars.com/kata/5ab6538b379d20ad880000ab."""


def area_or_perimeter(length: int, width: int) -> int:
    return (length * 2 + 2 * width) if length != width else length ** 2

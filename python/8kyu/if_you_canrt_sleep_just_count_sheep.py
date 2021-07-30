"""Kata url: https://www.codewars.com/kata/5b077ebdaf15be5c7f000077."""


def count_sheep(n: int) -> str:
    return ''.join(f"{x + 1} sheep..." for x in range(n))

"""Kata url: https://www.codewars.com/kata/66e509f59c8b4118ac009930."""
cache = []

def register_transaction(n: int | float) -> list[str]:
    cache.append(f"${n:,.2f}")
    return cache
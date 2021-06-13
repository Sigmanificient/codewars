from typing import Tuple


def high_and_low(numbers: str) -> str:
    """Kata url: https://www.codewars.com/kata/554b4ac871d6813a03000035."""
    numbers: Tuple[int] = tuple(map(int, numbers.split(' ')))
    return f"{max(numbers)} {min(numbers)}"

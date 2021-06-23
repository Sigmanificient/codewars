from typing import Optional


def repeat_it(string: Optional[str], n: int) -> str:
    """Kata url: https://www.codewars.com/kata/557af9418895e44de7000053."""
    return string * n if isinstance(string, str) else 'Not a string'

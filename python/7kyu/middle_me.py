def middle_me(n: int, x: str, y: str) -> str:
    """Kata url: https://www.codewars.com/kata/59cd155d1a68b70f8e000117."""
    return x.center(n + 1, y) if not n % 2 else x

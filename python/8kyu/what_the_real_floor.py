def get_real_floor(n: int) -> int:
    """Kata url: https://www.codewars.com/kata/574b3b1599d8f897470018f6."""
    if n <= 0:
        return n

    return n - 1 if n < 13 else n - 2

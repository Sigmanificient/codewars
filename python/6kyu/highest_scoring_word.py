def high(x: str) -> str:
    """Kata url: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272."""
    return max(x.split(" "), key=lambda v: sum(ord(y) - 96 for y in v))

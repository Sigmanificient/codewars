def get_middle(s: str) -> str:
    """Kata url: https://www.codewars.com/kata/56747fd5cb988479af000028"""
    length: int = len(s)
    middle: int = length // 2
    return s[middle - (not length % 2):middle + 1]

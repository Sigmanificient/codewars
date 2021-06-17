def remove(s: str) -> str:
    """Kata url: https://www.codewars.com/kata/57fae964d80daa229d000126/solutions/python."""
    return s[:-1] if s.endswith('!') else s

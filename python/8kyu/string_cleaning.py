def string_clean(s: str) -> str:
    """Kata url: https://www.codewars.com/kata/57e1e61ba396b3727c000251."""
    return ''.join(c for c in s if not c.isdigit())

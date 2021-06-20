def ensure_question(s: str) -> str:
    """Kata url: https://www.codewars.com/kata/5866fc43395d9138a7000006."""
    return s if s.endswith('?') else f"{s}?"

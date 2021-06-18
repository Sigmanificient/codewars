def to_alternating_case(string: str) -> str:
    """Kata url: https://www.codewars.com/kata/56efc695740d30f963000557."""
    return ''.join(char.lower() if char.isupper() else char.upper() for char in string)

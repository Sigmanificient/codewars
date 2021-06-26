def shortcut(s: str) -> str:
    """Kata url: https://www.codewars.com/kata/5547929140907378f9000039."""
    return ''.join(x for x in s if x not in 'aeiou')

def replace_exclamation(s: str) -> str:
    """Kata url: https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed."""
    return ''.join('!' if char.lower() in 'aeiou' else char for char in s)
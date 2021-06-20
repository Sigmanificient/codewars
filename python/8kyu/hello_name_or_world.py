def hello(name: str = '') -> str:
    """Kata url: https://www.codewars.com/kata/57e3f79c9cb119374600046b."""
    return f"Hello, {name.capitalize() if name else 'World'}!"

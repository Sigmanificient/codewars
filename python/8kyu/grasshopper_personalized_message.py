def greet(name: str, owner: str) -> str:
    """Kata url: https://www.codewars.com/kata/5772da22b89313a4d50012f7."""
    return 'Hello {}'.format("boss" if name == owner else "guest")

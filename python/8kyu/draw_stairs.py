def draw_stairs(n: int) -> str:
    """Kata url: https://www.codewars.com/kata/5b4e779c578c6a898e0005c5."""
    return '\n'.join(' ' * i + 'I' for i in range(n))

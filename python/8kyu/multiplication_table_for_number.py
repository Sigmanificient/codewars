def multi_table(number: int) -> str:
    """Kata url: https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce."""
    return '\n'.join(f"{i} * {number} = {i * number}" for i in range(1, 11))

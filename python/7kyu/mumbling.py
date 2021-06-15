def accum(s: str) -> str:
    """Kata url: codewars.com/kata/5667e8f4e3f572a8f2000039."""
    return '-'.join((x * (i + 1)).capitalize() for i, x in enumerate(s))

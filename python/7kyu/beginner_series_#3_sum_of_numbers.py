def get_sum(a: int, b: int) -> int:
    """Kata url: https://www.codewars.com/kata/55f2b110f61eb01779000053."""
    if b < a:
        a, b = b, a

    return sum(range(a, b + 1))

def max_redigit(num: int) -> int:
    """Kata url: https://www.codewars.com/kata/563700da1ac8be8f1e0000dc."""
    if 99 < num < 1000:
        return int(''.join(sorted(str(abs(num)), reverse=True)))

def descending_order(num: int) -> int:
    """Kata url: https://www.codewars.com/kata/5467e4d82edf8bbf40000155."""
    return int(''.join(sorted(str(num), reverse=True)))

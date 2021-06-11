def dig_pow(n: int, p: int) -> int:
    """Kata url: https://www.codewars.com/kata/5552101f47fc5178b1000050."""
    r = 0
    for digit in str(n):
        r += int(digit) ** p
        p += 1

    return r // n if (r % n) == 0 else -1

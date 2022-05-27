"""Kata url: https://www.codewars.com/kata/546e2562b03326a88e000020/. """


def square_digits(num: int) -> int:
    return int(''.join(str(int(digit) ** 2) for digit in str(num)))

"""Kata url: https://www.codewars.com/kata/5a2b703dc5e2845c0900005a."""

def is_divide_by(number: int, a: int, b: int) -> bool:
    return (number / a).is_integer() and (number / b).is_integer()

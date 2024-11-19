"""Kata url: https://www.codewars.com/kata/670b97a21ee38d40e1cf26ee."""

def to_scientific(num):
    n = str(num)
    if num < 5e3:
        return n
    return f"{n[0]}.{n[1:4].rstrip('0') or '0'}e{len(n)-1}"
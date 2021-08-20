# Kata url: https://www.codewars.com/kata/574b1916a3ebd6e4fa0012e7.

def is_opposite(s1: str, s2: str) -> bool:
    return len(s1) and s1 == s2.swapcase()

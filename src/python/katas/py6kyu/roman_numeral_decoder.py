"""Kata url: https://www.codewars.com/kata/51b6249c4612257ac0000005."""

romans = {
    'M': 1_000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def solution(roman: str) -> int:
    last = n = 0

    for v in (romans[c] for c in roman[::-1]):
        n += v if v >= last else -v
        last = v
    return n
"""Kata url: https://www.codewars.com/kata/5a1560c980171f3f68000037."""
from string import ascii_lowercase

VOWELS = "aeiou"
CONSONANTS = ''.join(c for c in ascii_lowercase if c not in VOWELS)


def palindrome(s):
    s = s.lower()
    vowels = [c for c in s if c in VOWELS]
    consonants = [c for c in s if c in CONSONANTS]
    score = (vowels == vowels[::-1]) + 2*(consonants == consonants[::-1])
    return {
        0: "neither",
        1: "vowel",
        2: "consonant",
        3: "both"
    }.get(score)
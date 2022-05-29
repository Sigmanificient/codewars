"""Kata url: https://www.codewars.com/kata/597754ba62f8a19c98000030."""


def vowel_change(txt: str, vow: str) -> str:
    return txt.translate(str.maketrans('aeiou', vow * 5))

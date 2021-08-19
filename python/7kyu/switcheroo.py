"""Kata url: https://www.codewars.com/kata/57f759bb664021a30300007d."""


def switcheroo(s: str) -> str:
    return s.translate(str.maketrans('ab', 'ba'))

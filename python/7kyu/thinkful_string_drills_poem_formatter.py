"""Kata url: https://www.codewars.com/kata/585af8f645376cda59000200."""


def format_poem(poem: str) -> str:
    return '.\n'.join(poem.split('. '))

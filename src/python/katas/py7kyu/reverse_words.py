"""Kata url: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4."""


def reverse_words(text: str) -> str:
    return " ".join(word[::-1] for word in text.split(" "))

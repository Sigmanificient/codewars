"""Kata url: https://www.codewars.com/kata/6097a9f20d32c2000d0bdb98."""


def i(word: str) -> str:
    if not word:
        return 'Invalid word'

    if word[0] == 'I' or word[0].islower():
        return 'Invalid word'

    vowels = sum(True for v in word.lower() if v in 'aeiou')

    if len(word) - vowels <= vowels:
        return 'Invalid word'

    return f"i{word}"

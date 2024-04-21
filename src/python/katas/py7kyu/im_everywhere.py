"""Kata url: https://www.codewars.com/kata/6097a9f20d32c2000d0bdb98."""


INVALID = "Invalid word" 


def i(word: str) -> str:
    if not word:
        return INVALID

    if word[0] == "I" or word[0].islower():
        return INVALID

    vowels = sum(True for v in word.lower() if v in "aeiou")

    if len(word) - vowels <= vowels:
        return INVALID

    return f"i{word}"


def test_i():
    assert i("Phone") == "iPhone"
    assert i("World") == "iWorld"
    assert i("Human") == "iHuman"
    assert i("Programmer") == "iProgrammer"
    assert i("") == INVALID
    assert i("Inspire") == INVALID
    assert i("East") == INVALID
    assert i("Peace") == INVALID
    assert i("road") == INVALID
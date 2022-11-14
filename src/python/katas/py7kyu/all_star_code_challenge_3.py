"""Kata url: https://www.codewars.com/kata/58640340b3a675d9a70000b9."""


def remove_vowels(strng):
    return ''.join(char for char in strng if char not in 'aeiou')


def test_remove_vowels():
    assert remove_vowels("drake") == "drk"
    assert remove_vowels("aeiou") == ""

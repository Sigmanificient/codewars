"""Kata url: https://www.codewars.com/kata/52fba66badcd10859f00097e."""


def disemvowel(string):
    return ''.join(char for char in string if char.lower() not in 'aeiou')


def test_disemvowel():
    assert disemvowel("") == ""
    assert disemvowel("aeiou") == ""
    assert disemvowel("AEIOU") == ""

    assert disemvowel("Hello, world!") == "Hll, wrld!"
    assert disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"

"""Kata url: https://www.codewars.com/kata/58b8c94b7df3f116eb00005b."""


def reverse_letter(string: str) -> str:
    return "".join(filter(str.isalpha, string[::-1]))


def test_reverse_letter():
    assert reverse_letter("krishan") == "nahsirk"
    assert reverse_letter("ultr53o?n") == "nortlu"
    assert reverse_letter("ab23c") == "cba"
    assert reverse_letter("krish21an") == "nahsirk"

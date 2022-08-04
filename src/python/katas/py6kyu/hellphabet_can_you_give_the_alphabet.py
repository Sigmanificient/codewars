"""Kata url: https://www.codewars.com/kata/62dcbe87f4ac96005f052962."""
ALPHABET = str().join(x for x in sorted(set(str().join(dir(int)))) if x.isalpha())


def test_alphabet():
    assert ALPHABET == "abcdefghijklmnopqrstuvwxyz"

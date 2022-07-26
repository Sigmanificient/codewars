"""Kata url: https://www.codewars.com/kata/5264d2b162488dc400000001."""


def spin_words(sentence: str) -> str:
    return " ".join(w if len(w) < 5 else w[::-1] for w in sentence.split(" "))


def test_spin_words():
    assert spin_words("Welcome") == "emocleW"
    assert spin_words("to") == "to"
    assert spin_words("CodeWars") == "sraWedoC"
    assert spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes"

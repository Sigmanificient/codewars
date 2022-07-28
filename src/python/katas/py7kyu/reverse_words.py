"""Kata url: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4."""


def reverse_words(text: str) -> str:
    return " ".join(word[::-1] for word in text.split(" "))


def test_reverse_words():
    assert reverse_words("") == ""

    assert reverse_words(
        "The greatest victory is that which requires no battle"
    ) == "ehT tsetaerg yrotciv si taht hcihw seriuqer on elttab"

    assert reverse_words(
        "Lorem ipsum dolor sit amet"
    ) == "meroL muspi rolod tis tema"

"""Kata url: https://www.codewars.com/kata/546f922b54af40e1e90001da."""

alphabet: str = "abcdefghijklmnopqrstuvwxyz"


def alphabet_position(text: str) -> str:
    return ' '.join(
        str(alphabet.index(char) + 1)
        for char in text.lower()
        if char in alphabet
    )


def test_alphabet_position():
    from random import randint

    r1 = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    r2 = "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"

    assert alphabet_position("The sunset sets at twelve o' clock.") == r1
    assert alphabet_position("The narwhal bacons at midnight.") == r2

    number_test = ''.join(str(randint(1, 9)) for _ in range(10))
    assert alphabet_position(number_test) == ""

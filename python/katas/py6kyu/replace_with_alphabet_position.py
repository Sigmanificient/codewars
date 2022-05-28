"""Kata url: https://www.codewars.com/kata/546f922b54af40e1e90001da."""

alphabet: str = "abcdefghijklmnopqrstuvwxyz"


def alphabet_position(text: str) -> str:
    return ' '.join(
        str(alphabet.index(char) + 1)
        for char in text.lower()
        if char in alphabet
    )

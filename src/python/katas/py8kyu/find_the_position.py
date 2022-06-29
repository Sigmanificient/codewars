"""Kata url: https://www.codewars.com/kata/5808e2006b65bff35500008f."""


def position(alphabet: str) -> str:
    return f'Position of alphabet: {"abcdefghijklmnopqrstuvwxyz".index(alphabet) + 1}'


def test_position():
    assert position("a") == "Position of alphabet: 1"
    assert position("z") == "Position of alphabet: 26"
    assert position("e") == "Position of alphabet: 5"

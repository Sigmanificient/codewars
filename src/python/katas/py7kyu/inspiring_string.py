"""Kata url: https://www.codewars.com/kata/5939ab6eed348a945f0007b2."""


def longest_word(words):
    return sorted(words.split(' '), key=len)[-1]


def test_longest_word():
    assert longest_word('a b c d e fgh') == "fgh"
    assert longest_word('one two three') == "three"
    assert longest_word('red blue grey') == "grey"

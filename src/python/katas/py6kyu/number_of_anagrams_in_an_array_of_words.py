"""Kata url: https://www.codewars.com/kata/587e18b97a25e865530000d8."""


def anagram_counter(words):
    return sum(
        1 for c, word in enumerate(words)
        for pair in words[c + 1:]
        if sorted(word) == sorted(pair)
    )


def test_anagram_counter():
    assert anagram_counter([]) == 0
    assert anagram_counter(['dell', 'ledl', 'abc', 'cba']) == 2
    assert anagram_counter(['dell', 'ledl', 'lled', 'cba']) == 3
    assert anagram_counter(
        ['dell', 'ledl', 'abc', 'cba', 'bca', 'bac', 'cab']
    ) == 11

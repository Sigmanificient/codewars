"""Kata url: https://www.codewars.com/kata/5697fb83f41965761f000052."""


def filter_long_words(sentence, n):
    return [w for w in sentence.split(' ') if len(w) > n]


def test_filer_long_words():
    assert filter_long_words(
        "The quick brown fox jumps over the lazy dog", 4
    ) == ['quick', 'brown', 'jumps']

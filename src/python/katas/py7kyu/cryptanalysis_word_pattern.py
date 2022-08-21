"""Kata url: https://www.codewars.com/kata/5f3142b3a28d9b002ef58f5e."""
from typing import Dict


def word_pattern(word: str) -> str:
    chars: Dict[str, int] = {}
    k = 0

    out = []
    for c in word.lower():
        i = chars.get(c)

        if i is None:
            chars[c] = k
            i = k
            k += 1

        out.append(i)

    return '.'.join(map(str, out))


def test_word_pattern():
    assert word_pattern("hello") == "0.1.2.2.3"
    assert word_pattern("heLlo") == "0.1.2.2.3"
    assert word_pattern("helLo") == "0.1.2.2.3"

    assert word_pattern("Hippopotomonstrosesquippedaliophobia") == (
        "0.1.2.2.3.2.3.4.3.5.3.6.7.4.8.3.7.9.7.10.11.1.2.2.9.12.13.14.1.3.2.0.3"
        ".15.1.13"
    )

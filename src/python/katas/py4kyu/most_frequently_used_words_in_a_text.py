"""Kata url: https://www.codewars.com/kata/51e056fe544cf36c410000fb."""

from collections import defaultdict
from string import ascii_lowercase


def top_3_words(text):
    allowed = ascii_lowercase + "'"
    counter = defaultdict(int)
    word = ""

    for char in f"{text} ":
        c = char.lower()

        if c in allowed:
            word += c
            continue

        if word and set(word) != {"'"}:
            counter[word] += 1
            word = ""

    return sorted(counter.keys(), key=lambda x: counter[x], reverse=True)[:3]


def test_top_3_words():
    assert top_3_words("a a a  b  c c  d d d d  e e e e e") == ["e", "d", "a"]
    assert top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), [
        "e",
        "ddd",
        "aa",
    ]
    assert top_3_words("  //wont won't won't ") == ["won't", "wont"]
    assert top_3_words("  , e   .. ") == ["e"]
    assert top_3_words("  ...  ") == []
    assert top_3_words("  '  ") == []
    assert top_3_words("  '''  ") == []
    assert top_3_words(
        """In a village of La Mancha, the name of which I have no desire to call
        to mind, there lived not long since one of those gentlemen that keep a 
        lance in the lance-rack, an old buckler, a lean hack, and a greyhound
        for coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so 
        extra on Sundays, made away with three-quarters of his income."""
    ), ["a", "of", "on"]

"""Kata url: https://www.codewars.com/kata/52b305bec65ea40fe90007a7."""
from typing import List


def grabscrab(word: str, possible_words: List[str]) -> List[str]:
    letters = sorted(word)
    return [
        p_word
        for p_word in possible_words
        if sorted(p_word) == letters
    ]


def test_grabscrab():
    assert grabscrab("trisf", ["first"]) == ["first"]
    assert grabscrab("oob", ["bob", "baobab"]) == []

    assert grabscrab(
        "ainstuomn", ["mountains", "hills", "mesa"]
    ) == ["mountains"]

    assert grabscrab(
        "oolp", ["donkey", "pool", "horse", "loop"]
    ) == ["pool", "loop"]

    assert grabscrab(
        "ortsp", ["sport", "parrot", "ports", "matey"]
    ) == ["sport", "ports"]

    assert grabscrab("ourf", ["one", "two", "three"]) == []

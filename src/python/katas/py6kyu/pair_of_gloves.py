"""Kata url: https://www.codewars.com/kata/58235a167a8cb37e1a0000db."""
from collections import defaultdict


def number_of_pairs(gloves):
    pairs = defaultdict(int)

    for glove in gloves:
        pairs[glove] += 1

    return sum(
        glove_count // 2
        for glove_count in pairs.values()
    )


def test_number_of_pairs():
    assert number_of_pairs(["red", "red"]) == 1
    assert number_of_pairs(["red", "green", "blue"]) == 0
    assert number_of_pairs(
        ["gray", "black", "purple", "purple", "gray", "black"]
    ) == 3
    assert number_of_pairs([]) == 0
    assert number_of_pairs(
        ["red", "green", "blue", "blue", "red", "green", "red", "red", "red"]
    ) == 4

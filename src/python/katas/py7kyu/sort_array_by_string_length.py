"""Kata url: https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c."""

from typing import List


def sort_by_length(arr: List[str]) -> List[str]:
    return sorted(arr, key=len)


def test_sort_by_length():
    assert sort_by_length(["beg", "life", "i", "to"]) == ["i", "to", "beg", "life"]
    assert sort_by_length(["", "moderately", "brains", "pizza"]) == [
        "",
        "pizza",
        "brains",
        "moderately",
    ]
    assert sort_by_length(["longer", "longest", "short"]) == [
        "short",
        "longer",
        "longest",
    ]
    assert sort_by_length(["dog", "food", "a", "of"]) == ["a", "of", "dog", "food"]
    assert sort_by_length(["", "dictionary", "eloquent", "bees"]) == [
        "",
        "bees",
        "eloquent",
        "dictionary",
    ]
    assert sort_by_length(
        ["a longer sentence", "the longest sentence", "a short sentence"]
    ) == ["a short sentence", "a longer sentence", "the longest sentence"]

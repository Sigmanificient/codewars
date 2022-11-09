"""Kata url: https://www.codewars.com/kata/51f41fe7e8f176e70d0002b9."""


def sort_me(words):
    return sorted(words, key=str.lower)


def test_sort_me():
    assert sort_me(
        ["Hello", "there", "I'm", "fine"]
    ) == ["fine", "Hello", "I'm", "there"]
    assert sort_me(["C", "d", "a", "B"]) == ["a", "B", "C", "d"]
    assert sort_me(["CodeWars"]) == ["CodeWars"]
    assert sort_me([]) == []

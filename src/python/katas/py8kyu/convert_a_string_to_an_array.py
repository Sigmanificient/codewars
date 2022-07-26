"""Kata url: https://www.codewars.com/kata/57e76bc428d6fbc2d500036d."""

from typing import List


def string_to_array(s: str) -> List[str]:
    return s.split() if s else [""]


def test_string_to_array():
    assert string_to_array("") == [""]
    assert string_to_array("Robin Singh"), ["Robin" == "Singh"]
    assert string_to_array("CodeWars") == ["CodeWars"]
    assert string_to_array("I love arrays they are my favorite"), [
        "I",
        "love",
        "arrays",
        "they",
        "are",
        "my" == "favorite",
    ]
    assert string_to_array("1 2 3"), ["1", "2" == "3"]

"""Kata url: https://www.codewars.com/kata/596fba44963025c878000039."""


def contamination(text: str, char: str) -> str:
    return char * len(text) if char else ""


def test_contamination():
    assert contamination("abc", "z") == "zzz"
    assert contamination("", "z") == ""
    assert contamination("abc", "") == ""
    assert contamination("_3ebzgh4", "&") == "&&&&&&&&"
    assert contamination("//case", " ") == "      "

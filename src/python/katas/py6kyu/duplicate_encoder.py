"""Kata url: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c."""


def duplicate_encode(word: str) -> str:
    word = word.lower()
    return "".join("(" if word.count(c) == 1 else ")" for c in word)


def test_duplicate_encoder():
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("

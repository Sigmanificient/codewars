"""Kata url: https://www.codewars.com/kata/5704aea738428f4d30000914."""


def triple_trouble(one: str, two: str, three: str) -> str:
    return "".join(a + b + c for a, b, c in zip(one, two, three))


def test_triple_trouble():
    assert triple_trouble("aaa", "bbb", "ccc") == "abcabcabc"
    assert triple_trouble("aaaaaa", "bbbbbb", "cccccc") == "abcabcabcabcabcabc"
    assert triple_trouble("burn", "reds", "roll") == "brrueordlnsl"
    assert triple_trouble("Bm", "aa", "tn") == "Batman"
    assert triple_trouble("LLh", "euo", "xtr") == "LexLuthor"

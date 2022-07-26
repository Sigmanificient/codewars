"""Kata url: https://www.codewars.com/kata/57f759bb664021a30300007d."""


def switcheroo(s: str) -> str:
    return s.translate(str.maketrans("ab", "ba"))


def test_switcheroo():
    assert switcheroo("abc") == "bac"
    assert switcheroo("aaabcccbaaa") == "bbbacccabbb"
    assert switcheroo("ccccc") == "ccccc"
    assert switcheroo("abababababababab") == "babababababababa"
    assert switcheroo("aaaaa") == "bbbbb"

"""Kata url: https://www.codewars.com/kata/53dc23c68a0c93699800041d."""


from typing import List


def smash(words: List[str]) -> str:
    return ' '.join(words)


def test_smash():
    assert smash([]) == ""
    assert smash(["hello"]) == "hello"
    assert smash(["hello", "world"]) == "hello world"
    assert smash(["hello", "amazing", "world"]) == "hello amazing world"
    assert smash(["this", "is", "a", "really", "long", "sentence"]) == "this is a really long sentence"


"""Kata url: https://www.codewars.com/kata/56f695399400f5d9ef000af5."""


def correct_tail(body: str, tail: str) -> bool:
    return body.endswith(tail)


def test_correct_tail():
    assert correct_tail("Fox", "x")
    assert correct_tail("Rhino", "o")
    assert correct_tail("Meerkat", "t")
    assert not correct_tail("Emu", "t")
    assert not correct_tail("Badger", "s")
    assert not correct_tail("Giraffe", "d")

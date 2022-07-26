"""Kata url: https://www.codewars.com/kata/53369039d7ab3ac506000467."""


def bool_to_word(boolean: bool) -> str:
    return "Yes" if boolean else "No"


def test_bool_to_word():
    assert bool_to_word(True) == "Yes"
    assert bool_to_word(False) == "No"

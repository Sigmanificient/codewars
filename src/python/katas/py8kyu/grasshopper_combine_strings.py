"""Kata url: https://www.codewars.com/kata/55f73f66d160f1f1db000059."""


def combine_names(a: str, b: str) -> str:
    return f"{a} {b}"


def test_combine_names():
    assert combine_names("James", "Stevens") == "James Stevens"
    assert combine_names("Davy", "Back") == "Davy Back"
    assert combine_names("Arthur", "Dent") == "Arthur Dent"

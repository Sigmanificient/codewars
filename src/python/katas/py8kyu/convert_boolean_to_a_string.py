"""Kata url: https://www.codewars.com/kata/551b4501ac0447318f0009cd."""


def boolean_to_string(b: bool) -> str:
    return str(b)


def test_bool_to_string():
    assert boolean_to_string(True) == "True"
    assert boolean_to_string(False) == "False"

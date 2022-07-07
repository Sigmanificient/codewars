"""Kata url: https://www.codewars.com/kata/55c90cad4b0fe31a7200001."""


def build_string(*args):
    return f"I like {', '.join(args)}!"


def test_build_string():
    assert build_string('Cheese', 'Milk', 'Chocolate') == 'I like Cheese, Milk, Chocolate!'
    assert build_string('Cheese', 'Milk') == 'I like Cheese, Milk!'
    assert build_string('Chocolate') == 'I like Chocolate!'

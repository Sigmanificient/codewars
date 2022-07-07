"""Kata url: https://www.codewars.com/kata/50ee6b0bdeab583673000025."""

a: str = "code"
b: str = "wa.rs"
name: str = a + b


def test_solution():
    assert name == "codewa.rs"
    assert len(name) == 9

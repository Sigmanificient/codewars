"""Kata url: https://www.codewars.com/kata/5612e743cab69fec6d000077."""

a: str = "dev"
b: str = "Lab"

name: str = a + b


def test_solution():
    assert a == 'dev'
    assert b == 'Lab'
    assert name == 'devLab'

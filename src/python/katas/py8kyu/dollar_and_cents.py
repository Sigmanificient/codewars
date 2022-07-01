"""Kata url: https://www.codewars.com/kata/55902c5eaa8069a5b4000083."""


def format_money(amount: int) -> str:
    return f"${amount:.2f}"


def test_format_money():
    assert format_money(0) == '$0.00'
    assert format_money(39.99) == '$39.99'
    assert format_money(1000000000) == '$1000000000.00'

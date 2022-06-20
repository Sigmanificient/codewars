"""Kata url: https://www.codewars.com/kata/5966e33c4e686b508700002d."""


def sum_str(a: str, b: str) -> str:
    return f"{int(f'0{a}') + int(f'0{b}')}"


def test_sum_str():
    assert sum_str("4", "5") == "9"
    assert sum_str("34", "5") == "39"

    assert sum_str("9", "") == "9"
    assert sum_str("", "9") == "9"
    assert sum_str("", "") == "0"

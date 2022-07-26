"""Kata url: https://www.codewars.com/kata/5b077ebdaf15be5c7f000077."""


def count_sheep(n: int) -> str:
    return "".join(f"{x + 1} sheep..." for x in range(n))


def test_count_sheep():
    assert count_sheep(0) == ""
    assert count_sheep(1) == "1 sheep..."
    assert count_sheep(2) == "1 sheep...2 sheep..."
    assert count_sheep(3) == "1 sheep...2 sheep...3 sheep..."

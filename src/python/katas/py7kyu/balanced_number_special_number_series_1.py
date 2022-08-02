"""Kata url: https://www.codewars.com/kata/5a4e3782880385ba68000018."""


def balanced_num(number: int) -> str:
    n_str = str(number)
    half = len(n_str) // 2
    odd_length = not len(n_str) % 2

    return 'Not ' * (
        sum(map(int, n_str[:half - odd_length]))
        != sum(map(int, n_str[half + 1:]))
    ) + 'Balanced'


def test_balanced_num():
    assert balanced_num(7) == "Balanced"
    assert balanced_num(959) == "Balanced"
    assert balanced_num(13) == "Balanced"
    assert balanced_num(432) == "Not Balanced"
    assert balanced_num(424) == "Balanced"

    assert balanced_num(1024) == "Not Balanced"
    assert balanced_num(66545) == "Not Balanced"
    assert balanced_num(295591) == "Not Balanced"
    assert balanced_num(1230987) == "Not Balanced"
    assert balanced_num(56239814) == "Balanced"

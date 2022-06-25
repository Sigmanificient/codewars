"""Kata url: https://www.codewars.com/kata/5709bdd2f088096786000008."""


def super_size(n: int) -> int:
    return int(''.join(sorted(str(n), reverse=True)))


def test_super_size():
    assert super_size(0) == 0
    assert super_size(2) == 2
    assert super_size(69) == 96
    assert super_size(513) == 531
    assert super_size(2017) == 7210
    assert super_size(414) == 441
    assert super_size(666666) == 666666
    assert super_size(608719) == 987610
    assert super_size(123456789) == 987654321
    assert super_size(700000000001) == 710000000000

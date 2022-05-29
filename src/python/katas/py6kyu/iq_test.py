"""Kata url: https://www.codewars.com/kata/552c028c030765286c00007d."""


def iq_test(numbers: str) -> int:
    oddness = [x % 2 for x in map(int, numbers.split())]
    return oddness.index(sum(oddness) == 1) + 1


def test_iqs():
    assert iq_test("2 4 7 8 10") == 3
    assert iq_test("1 2 2") == 1

"""Kata url: https://www.codewars.com/kata/5813d19765d81c592200001a."""


def dont_give_me_five(start: int, end: int) -> int:
    return sum('5' not in str(k) for k in range(start, end + 1))


def test_dont_give_me_five():
    assert dont_give_me_five(1, 9) == 8
    assert dont_give_me_five(4, 17) == 12
    assert dont_give_me_five(1, 90) == 72
    assert dont_give_me_five(-4, 17) == 20
    assert dont_give_me_five(-4, 37) == 38
    assert dont_give_me_five(-14, -1) == 13
    assert dont_give_me_five(-14, -6) == 9

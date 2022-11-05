"""Kata url: https://www.codewars.com/kata/577b9960df78c19bca00007e."""


def find_digit(num, nth):
    if nth < 1:
        return -1
    return (
        int(rep[-nth])
        if len(rep := str(abs(num))) >= nth else 0
    )


def test_find_digit():
    assert find_digit(5673, 4) == 5
    assert find_digit(129, 2) == 2
    assert find_digit(-2825, 3) == 8
    assert find_digit(0, 20) == 0
    assert find_digit(65, 0) == -1
    assert find_digit(24, -8) == -1

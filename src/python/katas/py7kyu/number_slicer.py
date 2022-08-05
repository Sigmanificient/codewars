"""Kata url: https://www.codewars.com/kata/62ed49568f8ab450e82a298b."""


def get_left(n: int) -> int:
    length = len(s := str(n))
    return int(s[:length // 2 + length % 2])


def test_get_left():
    assert get_left(123456) == 123
    assert get_left(1234567) == 1234
    assert get_left(98765432) == 9876

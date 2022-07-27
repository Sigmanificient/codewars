"""Kata url: https://www.codewars.com/kata/57a37f3cbb99449513000cd8."""


def get_number_from_string(string: str) -> int:
    return int(''.join(x for x in string if x.isdigit()))


def test_number():
    assert get_number_from_string("1") == 1
    assert get_number_from_string("123") == 123
    assert get_number_from_string("this is number: 7") == 7
    assert get_number_from_string("$100 000 000") == 100000000
    assert get_number_from_string("hell5o wor6ld") == 56
    assert get_number_from_string("one1 two2 three3 four4 five5") == 12345

"""Kata url: https://www.codewars.com/kata/525f47c79f2f25a4db000025."""
import re


def valid_phone_number(phone_number: str) -> bool:
    return re.match(r"^\(\d{3}\) \d{3}-\d{4}$", phone_number) is not None


def test_valid_phone_number():
    assert valid_phone_number("(123) 456-7890")
    assert valid_phone_number("(333) 185-0594")
    assert not valid_phone_number("(1111)555 2345")
    assert not valid_phone_number("(098) 123 4567")
    assert not valid_phone_number("(123)456-7890")
    assert not valid_phone_number("abc(123)456-7890")
    assert not valid_phone_number("(123)456-7890abc")
    assert not valid_phone_number("abc(123)456-7890abc")
    assert not valid_phone_number("abc(123) 456-7890")
    assert not valid_phone_number("(123) 456-7890abc")
    assert not valid_phone_number("abc(123) 456-7890abc")

"""Kata url: https://www.codewars.com/kata/56833b76371e86f8b6000015."""
import re


def to_cents(amount):
    match = re.fullmatch(r'\$(\d+)\.(\d{2})', amount)
    return int(''.join(match.groups())) if match else None


def test_to_cents():
    assert to_cents("") is None
    assert to_cents("1") is None
    assert to_cents("1.23") is None
    assert to_cents("$1") is None
    assert to_cents("$1.23") == 123
    assert to_cents("$99.99") == 9999
    assert to_cents("$12345678.90") == 1234567890
    assert to_cents("$9.69") == 969
    assert to_cents("$9.70") == 970
    assert to_cents("$9.71") == 971
    assert to_cents("$1.23\n") is None
    assert to_cents("\n$1.23") is None
    assert to_cents("$0.69") == 69
    assert to_cents("$9.69$4.3.7") is None
    assert to_cents("$9.692") is None

"""Kata url: https://www.codewars.com/kata/586efc2dcf7be0f217000619."""


def reverse_slice(s):
    s = s[::-1]
    return [s[i:] for i in range(len(s))]


def test_reverse_slice():
    assert reverse_slice('123') == ['321', '21', '1']
    assert reverse_slice('abcde') == ['edcba', 'dcba', 'cba', 'ba', 'a']

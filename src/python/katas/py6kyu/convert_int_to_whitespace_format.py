"""Kata url: https://www.codewars.com/kata/55b350026cc02ac1a7000032."""


def whitespace_number(n):
    return '\t '[n >= 0] + ''.join(
        '\t '[x == '0'] for x in f'{abs(n):b}'.lstrip('0')
    ) + '\n'


def test_whitespace_number():
    assert whitespace_number(1) == " \t\n"
    assert whitespace_number(0) == " \n"
    assert whitespace_number(-1) == "\t\t\n"
    assert whitespace_number(2) == " \t \n"
    assert whitespace_number(-3) == "\t\t\t\n"

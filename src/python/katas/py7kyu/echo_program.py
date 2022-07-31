"""Kata url: https://www.codewars.com/kata/5c6dc504abcd1628cd174bea."""


def echo_program() -> str:
    return __import__('inspect').getsource(echo_program).strip()


def test_echo_program():
    assert echo_program() == (
        'def echo_program() -> str:\n    return __import__(\'inspect\')'
        '.getsource(echo_program).strip()'
    )

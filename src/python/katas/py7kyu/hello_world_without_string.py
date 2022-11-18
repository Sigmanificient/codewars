"""Kata url: https://www.codewars.com/kata/584c7b1e2cb5e1a727000047."""


def hello_world():
    return open.__doc__[-74:-72].join(
        map(str.capitalize, hello_world.__name__.split(chr(95)))
    ) + chr(33)


def test_hello_word():
    assert hello_world() == 'Hello, World!'

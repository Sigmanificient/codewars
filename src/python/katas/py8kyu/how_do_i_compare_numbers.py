"""Kata url: https://www.codewars.com/kata/55d8618adfda93c89600012e."""


def what_is(x: int) -> str:
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'


def test_what_is():
    assert what_is(0) == 'nothing'
    assert what_is(1) == 'nothing'
    assert what_is(123) == 'nothing'
    assert what_is(-1) == 'nothing'

    assert what_is(42) == 'everything'
    assert what_is(42 * 42) == 'everything squared'

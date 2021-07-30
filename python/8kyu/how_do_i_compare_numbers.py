"""Kata url: https://www.codewars.com/kata/55d8618adfda93c89600012e."""


def what_is(x: int) -> str:
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'

"""Kata url: https://www.codewars.com/kata/572b6b2772a38bc1e700007a."""


def uni_total(s: str) -> int:
    return sum(map(ord, s))


def test_uni_total():
    assert uni_total("a") == 97
    assert uni_total("b") == 98
    assert uni_total("c") == 99
    assert uni_total("") == 0
    assert uni_total("aaa") == 291
    assert uni_total("abc") == 294
    assert uni_total("Mary Had A Little Lamb") == 1873
    assert uni_total("Mary had a little lamb") == 2001
    assert uni_total("CodeWars rocks") == 1370
    assert uni_total("And so does Strive") == 1661

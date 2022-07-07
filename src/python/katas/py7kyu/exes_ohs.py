"""Kata url: https://www.codewars.com/kata/55908aad6620c066bc00002a."""


def xo(s: str) -> bool:
    s = s.lower()
    return s.count('x') == s.count('o')


def test_xo():
    assert xo('xo')
    assert xo('xxOo')
    assert not xo('xxxm')
    assert not xo('ooom')
    assert not xo('xxxoooxx')
    assert not xo('xx')
    assert not xo('Oo')

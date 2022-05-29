"""Kata url: https://www.codewars.com/kata/52e1476c8147a7547a000811."""
import re


regex: str = r'^((?=.*?\d+)(?=.*?[a-z]+)(?=.*?[A-Z]+))[A-Za-z\d]{6,}$'


def test_regex():
    def _search(string) -> bool:
        return bool(re.search(regex, string))

    assert _search('fjd3IR9')
    assert not _search('ghdfj32')
    assert not _search('DSJKHD23')
    assert not _search('dsF43')
    assert _search('4fdg5Fj3')
    assert not _search('DHSJdhjsU')
    assert not _search('fjd3IR9.;')
    assert not _search('fjd3  IR9')
    assert _search('djI38D55')
    assert not _search('a2.d412')
    assert not _search('JHD5FJ53')
    assert not _search('!fdjn345')
    assert not _search('jfkdfj3j')
    assert not _search('123')
    assert not _search('abc')
    assert _search('123abcABC')
    assert _search('ABC123abc')
    assert _search('Password123')

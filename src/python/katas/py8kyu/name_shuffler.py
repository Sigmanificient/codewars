"""Kata url: https://www.codewars.com/kata/559ac78160f0be07c200005a."""


def name_shuffler(str_: str) -> str:
    return ' '.join(str_.split()[::-1])


def test_name_shuffler():
    assert name_shuffler('john McClane') == 'McClane john'
    assert name_shuffler('Mary jeggins') == 'jeggins Mary'
    assert name_shuffler('tom jerry') == 'jerry tom'

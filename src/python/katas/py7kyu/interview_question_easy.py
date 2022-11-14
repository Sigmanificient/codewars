"""Kata url: https://www.codewars.com/kata/5b358a1e228d316283001892."""
from string import ascii_lowercase


def get_strings(city):
    city = city.lower()
    return ','.join(
        f"{c}:{'*' * city.count(c)}"
        for c in sorted(set(city), key=city.index)
        if c in ascii_lowercase
    )


def test_get_strings():
    assert get_strings("Chicago") == "c:**,h:*,i:*,a:*,g:*,o:*"
    assert get_strings("Bangkok") == "b:*,a:*,n:*,g:*,k:**,o:*"
    assert get_strings("Las Vegas") == "l:*,a:**,s:**,v:*,e:*,g:*"

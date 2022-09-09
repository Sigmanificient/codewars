"""Kata url: https://www.codewars.com/kata/5639bdcef2f9b06ce800005b."""


def make_string(s):
    return ''.join(w[0] for w in s.split(' '))


def test_make_string():
    assert make_string("a") == "a"
    assert make_string("a b c") == "abc"
    assert make_string("This Is A Test") == "TIAT"
    assert make_string("sees eyes xray yoat") == "sexy"
    assert make_string("brown eyes are nice") == "bean"
    assert make_string("cars are very nice") == "cavn"
    assert make_string("kaks de gan has a big head") == "kdghabh"

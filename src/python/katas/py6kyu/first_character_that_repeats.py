"""Kata url: https://www.codewars.com/kata/54f9f4d7c41722304e000bbb."""


def first_dup(s):
    return next(
        (c for c in sorted(set(s), key=s.index) if s.count(c) > 1),
        None
    )


def test_first_dup():
    assert first_dup('bar') is None
    assert first_dup('tweet') == 't'
    assert first_dup('Ode to Joy') == ' '
    assert first_dup('ode to joy') == 'o'
    assert first_dup('123123') == '1'
    assert first_dup('!@#$!@#$') == '!'
    assert first_dup('1a2b3a3c') == 'a'

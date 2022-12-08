"""Kata url: https://www.codewars.com/kata/57faf32df815ebd49e000117."""


def remove(s):
    return ' '.join(word.rstrip('!') for word in s.split())


def test_remove():
    assert remove('Hi!') == 'Hi'
    assert remove('Hi!!!') == 'Hi'
    assert remove('!Hi') == '!Hi'
    assert remove('!Hi!') == '!Hi'
    assert remove('Hi! Hi!') == 'Hi Hi'
    assert remove('!!!Hi !!hi!!! !hi') == '!!!Hi !!hi !hi'

"""Kata url: https://www.codewars.com/kata/62b3e38df90eac002c7a983f."""

import re


def unflat_backspace(match):
    n = match.groups()[1]

    if n is None:
        return '#'

    repeats = int(n)
    return '#' * repeats


def solve(s):
    s = re.sub(r'\[backspace\](\*(\d+))?', unflat_backspace, s)

    out = []

    for c in s:
        if c != '#':
            out.append(c)

        elif out:
            out.pop()

    return ''.join(out)


def test_solve():
    assert solve('abcde[backspace]') == 'abcd'
    assert solve('oopp[backspace]s') == 'oops'
    assert solve('ooppp[backspace][backspace]s') == 'oops'

    assert solve('[backspace]*1a') == 'a'
    assert solve('ooppp[backspace]*2s') == 'oops'
    assert solve('oop[backspace]*1oo[backspace]*2pppp[backspace]*3s') == 'oops'

    assert solve('') == ''
    assert solve('[backspace]') == ''
    assert solve('[backspace]*3a  [backspace]') == 'a '
    assert solve('No backspaces') == 'No backspaces'

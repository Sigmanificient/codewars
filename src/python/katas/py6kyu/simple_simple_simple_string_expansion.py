"""Kata url: https://www.codewars.com/kata/5ae326342f8cbc72220000d2."""


def string_expansion(s):
    out, mul = '', 1

    for c in s:
        if c.isdigit():
            mul = int(c)
        else:
            out += mul * c
    return out


def test_string_expansion():
    assert string_expansion('3D2a5d2f') == 'DDDaadddddff'
    assert string_expansion('4D1a8d4j3k') == 'DDDDaddddddddjjjjkkk'
    assert string_expansion('4D2a8d4j2f') == 'DDDDaaddddddddjjjjff'
    assert string_expansion('3n6s7f3n') == 'nnnssssssfffffffnnn'
    assert string_expansion('0d4n8d2b') == 'nnnnddddddddbb'
    assert string_expansion('0c3b1n7m') == 'bbbnmmmmmmm'
    assert string_expansion('7m3j4ik2a') == 'mmmmmmmjjjiiiikkkkaa'
    assert string_expansion('3A5m3B3Y') == 'AAAmmmmmBBBYYY'
    assert string_expansion('5M0L8P1') == 'MMMMMPPPPPPPP'
    assert string_expansion('2B') == 'BB'
    assert string_expansion('7M1n3K') == 'MMMMMMMnKKK'
    assert string_expansion('A4g1b4d') == 'Aggggbdddd'

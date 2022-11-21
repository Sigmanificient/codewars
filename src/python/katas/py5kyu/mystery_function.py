"""Kata url: https://www.codewars.com/kata/531963f82dde6fc8c800048a."""


def solved(s):
    if len(s) & 1:
        half = len(s) // 2
        s = s[:half] + s[half + 1:]

    return ''.join(sorted(s, key=ord))


def test_solved():
    assert solved("Hello World") == "HWdellloor"
    assert solved("foobar") == "abfoor"
    assert solved("I see what you did there!") == "     !Iaddeeeehhirsttuwy"
    assert solved("") == ""
    assert solved("abcd") == "abcd"
    assert solved("abcde") == "abde"

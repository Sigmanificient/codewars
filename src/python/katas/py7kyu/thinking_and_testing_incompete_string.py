"""Kata url: https://www.codewars.com/kata/56d9292cc11bcc3629000533."""


def _testit(s):
    if len(s) & 1:
        s += s[-1]

    return ''.join(
        chr((ord(a) + ord(b)) // 2)
        for a, b in zip(s[::2], s[1::2])
    )


def test_testit():
    assert _testit("") == ""
    assert _testit("a") == "a"
    assert _testit("b") == "b"
    assert _testit("aa") == "a"
    assert _testit("ab") == "a"
    assert _testit("bc") == "b"
    assert _testit("aaaa") == "aa"
    assert _testit("aaaaaa") == "aaa"

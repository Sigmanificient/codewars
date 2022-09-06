"""Kata url: https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991."""


def rev_rot(string, sz):
    if not string or sz <= 0:
        return ''

    length = len(string)
    if length < sz:
        return ''

    chunks = [string[i:i + sz] for i in range(0, length, sz)]
    out = []

    if len(chunks[-1]) != sz:
        chunks.pop()

    return ''.join(
        (
            chunk[1:] + chunk[0]
            if sum(int(d) ** 3 for d in chunk) % 2
            else chunk[::-1]
        )
        for chunk in chunks
    )


def test_rev_rot():
    assert rev_rot("123456987654", 6) == "234561876549"
    assert rev_rot("123456987653", 6) == "234561356789"
    assert rev_rot("66443875", 4) == "44668753"
    assert rev_rot("66443875", 8) == "64438756"
    assert rev_rot("664438769", 8) == "67834466"
    assert rev_rot("123456779", 8) == "23456771"
    assert rev_rot("", 8) == ""
    assert rev_rot("123456779", 0) == ""
    assert rev_rot("563000655734469485", 4) == "0365065073456944"

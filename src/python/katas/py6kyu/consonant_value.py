"""Kata url: https://www.codewars.com/kata/59c633e7dcc4053512000073."""


def solve(word: str) -> int:
    a = ord('a') - 1
    cons_subs = []
    sub = 0

    for char in word:
        if char in 'aeiou':
            cons_subs.append(sub)
            sub = 0

        else:
            sub += (ord(char) - a)

    return max(cons_subs)


def test_solve():
    assert solve("zodiac") == 26
    assert solve("chruschtschov") == 80
    assert solve("khrushchev") == 38
    assert solve("strength") == 57
    assert solve("catchphrase") == 73
    assert solve("twelfthstreet") == 103
    assert solve("mischtschenkoana") == 80

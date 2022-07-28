"""Kata url: https://www.codewars.com/kata/5ae43ed6252e666a6b0000a4."""


def shuffle(s: str) -> str:
    return f'{s[::2]}{s[1::2]}'


def jumbled_string(s: str, n: int) -> str:
    g = shuffle(s)
    cycle = 1
    while s != g:
        g = shuffle(g)
        cycle += 1

    for _ in range(n % cycle):
        s = shuffle(s)
    return s


def test_jumbled_string():
    assert jumbled_string("Such Wow!", 1) == "Sc o!uhWw"
    assert jumbled_string("better example", 2) == "bexltept merae"
    assert jumbled_string("qwertyuio", 2) == "qtorieuwy"
    assert jumbled_string("Greetings", 8) == "Gtsegenri"

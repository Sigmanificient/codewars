"""Kata url: https://www.codewars.com/kata/5c3433a4d828182e420f4197."""


def reverse(a):
    rev = ''.join(x[::-1] for x in a[::-1])
    out = []

    x = 0
    for i in a:
        out.append(rev[x: x + len(i)])
        x += len(i)
    return out


def test_reverse():
    assert (
        reverse(["I", "like", "big", "butts", "and", "I", "cannot", "lie!"])
        == ["!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"]
    )
    assert reverse(
        [
            "?kn", "ipnr", "utotst", "ra", "tsn", "iksr", "uo", "yer", "ofebta",
            "eote", "vahu", "oyodpm", "ir", "hsyn", "amwoH"
        ]
    ) == [
        "How", "many", "shrimp", "do", "you", "have", "to", "eat", "before",
        "your", "skin", "starts", "to", "turn", "pink?"
    ]

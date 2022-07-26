"""Kata url: https://www.codewars.com/kata/5663f5305102699bad000056."""


def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1

    return max(abs(len(x) - len(y)) for y in a2 for x in a1)


def test_mxdiflg():
    assert (
        mxdiflg(
            [
                "hoqq",
                "bbllkw",
                "oox",
                "ejjuyyy",
                "plmiis",
                "xxxzgpsssa",
                "xxwwkktt",
                "znnnnfqknaz",
                "qqquuhii",
                "dvvvwz",
            ],
            ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"],
        )
        == 13
    )

    assert (
        mxdiflg(
            [
                "ejjjjmmtthh",
                "zxxuueeg",
                "aanlljrrrxx",
                "dqqqaaabbb",
                "oocccffuucccjjjkkkjyyyeehh",
            ],
            ["bbbaaayddqbbrrrv"],
        )
        == 10
    )

    assert mxdiflg([], ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]) == -1

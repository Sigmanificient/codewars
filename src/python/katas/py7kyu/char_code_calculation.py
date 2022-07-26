"""Kata url: https://www.codewars.com/kata/55847fcd3e7dadc9f800005f."""


def calc(x: str) -> int:
    t = "".join(str(ord(c)) for c in x)
    return sum(map(int, t)) - sum(map(int, t.replace("7", "1")))


def test_calc():
    assert calc("abcdef") == 6
    assert calc("ifkhchlhfd") == 6
    assert calc("aaaaaddddr") == 30
    assert calc("jfmgklf8hglbe") == 6
    assert calc("jaam") == 12

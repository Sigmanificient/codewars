"""Kata url: https://www.codewars.com/kata/58223370aef9fc03fd000071."""


def dashatize(n: int) -> str:
    if not isinstance(n, int):
        return 'None'

    n_str = str(abs(n))
    if len(n_str) == 1:
        return n_str

    sep = '-'
    out = ''

    len_n = len(n_str) - 1
    for c, char in enumerate(n_str):
        odd = ord(char) % 2
        before = c and out[-1] != '-'

        out += f"{sep * (odd and before)}{char}{sep * (c != len_n and odd)}"

    return out


def test_dashatize():
    assert dashatize(0), "0"
    assert dashatize(-1), "1"
    assert dashatize(274), "2-7-4"
    assert dashatize(5311), "5-3-1-1"
    assert dashatize(86320), "86-3-20"
    assert dashatize(974302), "9-7-4-3-02"
    assert dashatize(None), "None"
    assert dashatize(-28369), "28-3-6-9"

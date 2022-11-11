"""Kata url: https://www.codewars.com/kata/5818d00a559ff57a2f000082."""


class Pell:

    def get(self, n):
        a, b = 1, 0

        for i in range(n - 1):
            a, b = b + a * 2, a

        return a


def test_pell():
    pell = Pell()

    assert pell.get(1) == 1
    assert pell.get(2) == 2
    assert pell.get(3) == 5
    assert pell.get(4) == 12

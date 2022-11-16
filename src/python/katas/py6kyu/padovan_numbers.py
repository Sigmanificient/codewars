"""Kata url: https://www.codewars.com/kata/5803ee0ed5438edcc9000087."""


def padovan(n):
    a = b = c = 1

    for i in range(n):
        a, b, c = b, c, a + b

    return a


def test_padovan():
    assert padovan(0) == 1
    assert padovan(1) == 1
    assert padovan(2) == 1
    assert padovan(3) == 2
    assert padovan(4) == 2
    assert padovan(5) == 3
    assert padovan(6) == 4
    assert padovan(7) == 5
    assert padovan(8) == 7
    assert padovan(9) == 9

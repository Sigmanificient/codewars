"""Kata url: https://www.codewars.com/kata/5effa412233ac3002a9e471d."""


def add(num1: int, num2: int) -> str:
    ml = len(str(max(num1, num2)))

    def get_digits(k):
        return map(int, str(k).zfill(ml))

    out = ''
    for a, b in zip(
            get_digits(num1),
            get_digits(num2)
    ):
        out += str(a + b)

    return int(out)


def test_add():
    assert add(2, 11) == 13
    assert add(0, 1) == 1
    assert add(0, 0) == 0

    assert add(16, 18) == 214
    assert add(26, 39) == 515
    assert add(122, 81) == 1103

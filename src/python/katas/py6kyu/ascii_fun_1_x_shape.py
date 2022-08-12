"""Kata url: https://www.codewars.com/kata/5906436806d25f846400009b."""


def x(n: int) -> int:
    m = n - 1
    return '\n'.join(
        ''.join(
            '□■'[j == i or (m - i) == j]
            for j in range(n)
        ) for i in range(n)
    )


def test_x():
    assert x(3) == "■□■\n□■□\n■□■"
    assert x(7) == (
        "■□□□□□■\n□■□□□■□\n□□■□■□□\n"
        "□□□■□□□\n□□■□■□□\n□■□□□■□\n■□□□□□■"
    )

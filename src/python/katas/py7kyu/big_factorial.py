"""Kata url: https://www.codewars.com/kata/54f0d5447872e8ce9f00013d."""


def factorial(n: int) -> int:
    if n < 0:
        return None

    t = 1
    for i in range(1, n + 1):
        t *= i

    return t


def test_factorial():
    assert factorial(1) == 1
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(100) == int(
        "9332621544394415268169923885626670049071596826438162146859296389521759"
        "9993229915608941463976156518286253697920827223758251185210916864000000"
        "000000000000000000"
    )
    assert factorial(0) == 1
    assert factorial(-25) is None

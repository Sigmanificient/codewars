"""Kata url: https://www.codewars.com/kata/53d40c1e2f13e331fc000c26."""


def fib(n: int) -> int:
    """Calculates the nth Fibonacci number"""
    a, b = 0, 1
    for _ in range(abs(n)):
        a, b = b, a + b

    if n > 0:
        return a

    if n % 2:
        return a

    return -a


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5

    assert fib(1000) == int(
        '4346655768693745643568852767504062580256466051737178040248172908953655'
        '5417949051890403879840079255169295922593080322634775209689623239873322'
        '471161642996440906533187938298969649928516003704476137795166849228875'
    )

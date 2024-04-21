"""Kata url: https://www.codewars.com/kata/56b7771481290cc283000f28."""


def last_fib_digit(n):
    if not n % 60:
        return 0

    a, b = 1, 1
    for _ in range((n % 60) - 1):
        a, b = b, (a + b) % 10

    return a


def test_last_fib_digit():
    assert last_fib_digit(1) == 1
    assert last_fib_digit(21) == 6
    assert last_fib_digit(302) == 1
    assert last_fib_digit(4003) == 7
    assert last_fib_digit(50004) == 8
    assert last_fib_digit(600005) == 5
    assert last_fib_digit(7000006) == 3
    assert last_fib_digit(80000007) == 8
    assert last_fib_digit(900000008) == 1
    assert last_fib_digit(1000000009) == 9
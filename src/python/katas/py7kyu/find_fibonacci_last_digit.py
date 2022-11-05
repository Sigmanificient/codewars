"""Kata url: https://www.codewars.com/kata/56b7251b81290caf76000978."""


def get_last_digit(index):
    a, b = 1, 1

    for i in range(index - 1):
        a, b = b, (a + b) % 10

    return a


def test_get_last_digit():
    assert get_last_digit(193150) == 5
    assert get_last_digit(300) == 0
    assert get_last_digit(20001) == 6
    assert get_last_digit(800) == 5
    assert get_last_digit(1001) == 1
    assert get_last_digit(100) == 5
    assert get_last_digit(260) == 5
    assert get_last_digit(1111) == 9
    assert get_last_digit(1234) == 7
    assert get_last_digit(99999) == 6
    assert get_last_digit(10) == 5
    assert get_last_digit(234) == 2
    assert get_last_digit(193241) == 1
    assert get_last_digit(79) == 1
    assert get_last_digit(270) == 0

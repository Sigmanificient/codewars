"""Kata url: https://www.codewars.com/kata/534d0a229345375d520006a0."""


def power_of_two(n: int) -> bool:
    if not n:
        return False

    while n > 1:
        if n % 2:
            return False

        n //= 2

    return True


def test_power_of_two():
    assert not power_of_two(0)
    assert power_of_two(1)
    assert power_of_two(2)
    assert not power_of_two(5)
    assert not power_of_two(6)
    assert power_of_two(4096)

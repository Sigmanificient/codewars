"""Kata url: https://www.codewars.com/kata/57126304cdbf63c6770012bd."""


def is_digit(x: str) -> bool:
    try:
        _ = float(x)
        return True

    except ValueError:
        return False


def test_is_digit():
    assert not is_digit("s2324")
    assert is_digit("-234.4")

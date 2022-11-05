"""Kata url: https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed."""


def jumping_number(n):
    m = tuple(map(int, str(n)))
    return (
        "Jumping!!"
        if all(abs(y - x) == 1 for x, y in zip(m, m[1::]))
        else "Not!!"
    )


def test_jumping_number():
    assert jumping_number(1) == "Jumping!!"
    assert jumping_number(7) == "Jumping!!"
    assert jumping_number(9) == "Jumping!!"

    assert jumping_number(23) == "Jumping!!"
    assert jumping_number(32) == "Jumping!!"
    assert jumping_number(79) == "Not!!"
    assert jumping_number(98) == "Jumping!!"

    assert jumping_number(8987) == "Jumping!!"
    assert jumping_number(4343456) == "Jumping!!"
    assert jumping_number(98789876) == "Jumping!!"

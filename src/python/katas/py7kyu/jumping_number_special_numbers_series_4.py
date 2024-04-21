"""Kata url: https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed."""

JUMPING = "Jumping!!"


def jumping_number(n):
    m = tuple(map(int, str(n)))
    return (
        JUMPING
        if all(abs(y - x) == 1 for x, y in zip(m, m[1::]))
        else "Not!!"
    )


def test_jumping_number():
    assert jumping_number(1) == JUMPING
    assert jumping_number(7) == JUMPING
    assert jumping_number(9) == JUMPING

    assert jumping_number(23) == JUMPING
    assert jumping_number(32) == JUMPING
    assert jumping_number(79) == "Not!!"
    assert jumping_number(98) == JUMPING

    assert jumping_number(8987) == JUMPING
    assert jumping_number(4343456) == JUMPING
    assert jumping_number(98789876) == JUMPING
"""Kata url: https://www.codewars.com/kata/568d0dd208ee69389d000016."""


def rental_car_cost(d: int) -> int:
    total: int = 40 * d

    if d >= 7:
        total -= 50

    if 3 < d < 7:
        total -= 20

    return total


def test_get_rental_car_cost():
    assert rental_car_cost(1) == 40
    assert rental_car_cost(4) == 140
    assert rental_car_cost(7) == 230
    assert rental_car_cost(8) == 270

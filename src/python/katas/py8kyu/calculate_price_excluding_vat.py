"""Kata url: https://www.codewars.com/kata/5890d8bc9f0f422cf200006b."""


def excluding_vat_price(price):
    if price is None:
        return -1

    return round(price / 1.15, 2)


def test_excluding_vat_price():
    assert excluding_vat_price(230.00) == 200.00
    assert excluding_vat_price(123) == 106.96

"""Kata url: https://www.codewars.com/kata/56598d8076ee7a0759000087."""
from math import ceil

TIP = {
    'terrible': 0,
    'poor': 5,
    'good': 10,
    'great': 15,
    'excellent': 20
}


def calculate_tip(amount, rating):
    t = TIP.get(rating.lower(), 'Rating not recognised')
    return t if isinstance(t, str) else ceil((amount / 100) * t)


def test_calculate_tip():
    assert calculate_tip(30, "poor") == 2
    assert calculate_tip(20, "Excellent") == 4
    assert calculate_tip(20, "hi") == 'Rating not recognised'
    assert calculate_tip(107.65, "GReat") == 17
    assert calculate_tip(20, "great!") == 'Rating not recognised'

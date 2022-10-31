"""Kata url: https://www.codewars.com/kata/6359f0158f20011969cf0ebe."""
import re

def car_crash(road):
    return re.match(r'o.*[xX]', road)

def test_car_crash():
    assert not car_crash("O='`o ")
    assert not car_crash(" X \nX   O='`o\nX   ")
    assert not car_crash("O='`o                          ")
    assert car_crash("O='`o              x           ")
    assert car_crash("O='`o              X           ")
    assert car_crash(" X   X  X\nX         O='`o   X\nX   X   X  ")
    assert car_crash("O='`ox")

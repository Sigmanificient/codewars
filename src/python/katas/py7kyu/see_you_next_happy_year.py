"""Kata url: https://www.codewars.com/kata/5ae7e3f068e6445bc8000046."""


def next_happy_year(year: int) -> int:
    year += 1

    while len(set(str(year))) != 4:
        year += 1

    return year


def test_next_happy_year():
    assert next_happy_year(1001) == 1023
    assert next_happy_year(1123) == 1203
    assert next_happy_year(2001) == 2013
    assert next_happy_year(2334) == 2340
    assert next_happy_year(3331) == 3401
    assert next_happy_year(1987) == 2013
    assert next_happy_year(5555) == 5601
    assert next_happy_year(7712) == 7801
    assert next_happy_year(8088) == 8091
    assert next_happy_year(8999) == 9012


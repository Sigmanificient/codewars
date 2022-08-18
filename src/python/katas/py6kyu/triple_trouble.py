"""Kata url: https://www.codewars.com/kata/55d5434f269c0c3f1b000058."""


def triple_double(num1: int, num2: int) -> bool:
    a = str(num1)
    b = str(num2)

    return any(a.count(c) >= 3 and b.count(c) == 2 for c in set(a))


def test_triple_double():
    assert triple_double(451999277, 41177722899) == 1
    assert triple_double(1222345, 12345) == 0
    assert triple_double(12345, 12345) == 0
    assert triple_double(666789, 12345667) == 1
    assert triple_double(10560002, 100) == 1
    assert triple_double(1112, 122) == 0

"""Kata url: https://www.codewars.com/kata/56aed32a154d33a1f3000018."""


def my_first_kata(a, b):
    if type(a) != type(b) or type(b) != int:
        return False
    if not a or not b:
        return False
    return a % b + b % a


def test_my_first_kata():
    assert my_first_kata(3, 5) == (3 % 5 + 5 % 3)
    assert not my_first_kata("hello", 3)
    assert not my_first_kata(67, "bye")
    assert not my_first_kata(True, True)
    assert my_first_kata(314, 107) == (107 % 314 + 314 % 107)
    assert my_first_kata(1, 32) == (1 % 32 + 32 % 1)
    assert my_first_kata(-1, -1) == (-1 % -1 + -1 % -1)
    assert my_first_kata(19483, 9) == (9 % 19483 + 19483 % 9)
    assert not my_first_kata("hello", {})
    assert not my_first_kata([], "pippi")

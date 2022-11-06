"""Kata url: https://www.codewars.com/kata/5208fc3cb613bc725f000142."""


def solution(st, limit):
    return (c := st[:limit]) + ("..." * (c != st))


def test_solution():
    assert solution('Testing String', 3) == 'Tes...'
    assert solution('Testing String', 8) == 'Testing ...'
    assert solution('Test', 10) == 'Test'
    assert solution('Test', 4) == 'Test'

"""Kata url: https://www.codewars.com/kata/57089707fe2d01529f00024a."""


def check_alive(health: int) -> bool:
    return health > 0


def test_check_alive():
    assert check_alive(5)
    assert not check_alive(0)
    assert not check_alive(-5)
    assert not check_alive(-10)

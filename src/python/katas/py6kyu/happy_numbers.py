"""Kata url: https://www.codewars.com/kata/5464cbfb1e0c08e9b3000b3e."""


def is_happy(n):
    cache = set()
    if n == 1:
        return True

    while True:
        cache.add(n)
        n = sum(d ** 2 for d in map(int, str(n)))
        if n in cache:
            return False

        if n == 1:
            return True


def test_is_happy():
    assert is_happy(1)
    assert is_happy(7)
    assert is_happy(901)

    assert not is_happy(16)
    assert not is_happy(37)

"""Kata url: https://www.codewars.com/kata/5b0148133e9715bf6f000154."""


def hi_all():
    def Hello():
        pass

    def World():
        pass

    space = chr(len(str(ConnectionRefusedError)))
    return space.join((Hello.__name__, World.__name__))


def test_hi_all():
    assert hi_all() == "Hello World"

"""Kata url: https://www.codewars.com/kata/5b0148133e9715bf6f000154."""


def hi_all():
    def hello():
        """ dummy function for the name. """
        pass

    def world():
        """ dummy function for the name. """
        pass

    space = chr(len(str(ConnectionRefusedError)))
    return space.join((hello.__name__, world.__name__)).capitalize()


def test_hi_all():
    assert hi_all() == "Hello World"
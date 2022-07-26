"""Kata url: https://www.codewars.com/kata/53cf459503f9bbb774000003."""


class Python:
    def __init__(self, name):
        self.name = name


def test_cls():
    bubba = Python("Bubba")
    assert bubba.name == "Bubba"

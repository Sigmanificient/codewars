"""Kata url: https://www.codewars.com/kata/55c0ac142326fdf18d0000af."""


class Cube:

    def __init__(self, side=0):
        self.__side = side

    def get_side(self):
        return abs(self.__side)

    def set_side(self, new_side):
        self.__side = new_side


def text_cube():
    c = Cube()
    assert c.get_side() == 0

    c = Cube(10)
    assert c.get_side() == 10

    test_sides = [5, 10, -7, -9]
    for s in test_sides:
        c = Cube(s)
        assert c.get_side() == abs(s)

    for s in test_sides:
        c = Cube()
        c.set_side(s)
        assert c.get_side() == abs(s)

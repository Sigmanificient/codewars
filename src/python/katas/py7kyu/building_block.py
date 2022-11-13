"""Kata url: https://www.codewars.com/kata/55b75fcf67e558d3750000a3."""


class Block:

    def __init__(self, dimension):
        self.width, self.length, self.height = dimension

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_length(self):
        return self.length

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        return (
            self.width * self.height * 2
            + self.width * self.length * 2
            + self.height * self.length * 2
        )


def test_block():
    block1 = Block([2, 2, 2])
    assert block1.get_width() == 2
    assert block1.get_length() == 2
    assert block1.get_height() == 2
    assert block1.get_volume() == 8
    assert block1.get_surface_area() == 24

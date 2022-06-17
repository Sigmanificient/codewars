"""Kata url: https://www.codewars.com/kata/58261acb22be6e2ed800003a."""


def get_volume_of_cuboid(length: float, width: float, height: float) -> float:
    return length * width * height


def test_volume():
    assert get_volume_of_cuboid(1, 1, 1) == 1
    assert get_volume_of_cuboid(1, 2, 3) == 6
    assert get_volume_of_cuboid(2, 3, 4) == 24
    assert get_volume_of_cuboid(6.3, 2, 5) == 63

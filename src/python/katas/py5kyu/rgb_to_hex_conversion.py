"""Kata url: https://www.codewars.com/kata/513e08acc600c94f01000001."""


def rgb(r: int, g: int, b: int) -> str:
    return ''.join(
        f'{min(max(0, k), 255):02x}'
        for k in (r, g, b)
    ).upper()


def test_rgb():
    assert rgb(0, 0, 0) == "000000"
    assert rgb(1, 2, 3), "010203"
    assert rgb(255, 255, 255) == "FFFFFF"
    assert rgb(254, 253, 252) == "FEFDFC"
    assert rgb(-20, 275, 125) == "00FF7D"

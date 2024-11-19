"""Kata url: https://www.codewars.com/kata/56be4affc5dc03b84b001d2d."""

def get_reversed_color(hex_color):
    if not isinstance(hex_color, str) or len(hex_color) > 6:
        raise ValueError
    complementary = ((256**3) - int(hex_color.rjust(6, "0"), 16)) - 1
    return f"#{complementary:06X}"
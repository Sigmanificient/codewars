hot = "It's hotter than the sun!!"
not_hot = "Help yourself to a honeycomb Yorkie for the glovebox."


def apple(x):
    """Kata url: https://www.codewars.com/kata/580a094553bd9ec5d800007d."""
    return hot if int(x) ** 2 > 1000 else not_hot

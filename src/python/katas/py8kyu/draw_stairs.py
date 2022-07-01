"""Kata url: https://www.codewars.com/kata/5b4e779c578c6a898e0005c5."""


def draw_stairs(n: int) -> str:
    return '\n'.join(' ' * i + 'I' for i in range(n))


def test_draw_stairs():
    assert draw_stairs(1) == 'I'
    assert draw_stairs(3) == 'I\n I\n  I'
    assert draw_stairs(6) == 'I\n I\n  I\n   I\n    I\n     I'

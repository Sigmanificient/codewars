"""Kata url: https://www.codewars.com/kata/5c374b346a5d0f77af500a5a."""


def elevator(left, right, call):
    return (
        "left" if int(f'{left}{right}{call}') in {
            10, 20, 101, 102, 120, 121, 202, 212
        } else "right"
    )


def test_elevator():
    assert elevator(0, 1, 0)
    assert elevator(0, 1, 1)
    assert elevator(0, 1, 2)
    assert elevator(0, 0, 0)
    assert elevator(0, 2, 1)

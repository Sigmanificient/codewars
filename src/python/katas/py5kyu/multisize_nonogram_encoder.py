"""Kata url: https://www.codewars.com/kata/629049687438580064f0e6dd."""


def get_clues(group):
    clues = []
    current_clue = 0

    for item in group:
        if item:
            current_clue += 1
            continue

        if current_clue:
            clues.append(current_clue)
            current_clue = 0

    if current_clue:
        clues.append(current_clue)

    return tuple(clues)


def encode(nonogram):
    return (
        tuple(get_clues(col) for col in zip(*nonogram)),
        tuple(get_clues(line) for line in nonogram)
    )


def test_get_clues():
    assert get_clues((0, 0, 0, 0, 0)) == ()
    assert get_clues((0, 1)) == (1,)
    assert get_clues((1, 1, 1)) == (3,)
    assert get_clues((1, 0, 1, 1)) == (1, 2)
    assert get_clues((1, 0, 1, 0, 1, 0, 1)) == (1, 1, 1, 1)


def test_encode():
    assert encode(
        (
            (0, 0, 0, 0, 0),
            (1, 1, 1, 1, 1),
            (1, 1, 1, 1, 1),
            (0, 1, 1, 1, 0),
            (0, 0, 1, 0, 0),
        )
    ) == (
        ((2,), (3,), (4,), (3,), (2,)),
        ((), (5,), (5,), (3,), (1,))
    )

    assert encode(
        (
            (0, 1, 0, 1, 0),
            (1, 1, 0, 1, 1),
            (1, 1, 0, 1, 1),
            (0, 1, 0, 1, 0),
            (0, 0, 0, 0, 0),
        )
    ) == (
        ((2,), (4,), (), (4,), (2,)),
        ((1, 1), (2, 2), (2, 2), (1, 1), ())
    )

    assert encode(
        (
            (0, 0, 0, 1, 0, 0, 0, 1, 1, 0),
            (0, 0, 1, 1, 1, 0, 1, 1, 1, 1),
            (0, 0, 1, 1, 1, 1, 1, 1, 1, 1),
            (0, 0, 0, 1, 1, 1, 1, 1, 1, 0),
            (0, 0, 0, 0, 0, 1, 1, 0, 0, 0),
            (0, 1, 0, 0, 0, 0, 1, 1, 0, 0),
            (1, 0, 1, 0, 0, 0, 1, 1, 0, 0),
            (1, 1, 1, 0, 0, 1, 1, 0, 0, 0),
            (1, 1, 1, 0, 0, 1, 1, 1, 0, 1),
            (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
        )
    ) == (
        (
          (4,), (1, 3), (2, 4), (4, 1), (3, 1),
          (3, 3), (9,), (4, 2, 2), (4, 1), (2, 2)
        ),
        (
          (1, 2), (3, 4), (8,), (6,), (2,), (1, 2),
          (1, 1, 2), (3, 2), (3, 3, 1), (10,)
        )
    )

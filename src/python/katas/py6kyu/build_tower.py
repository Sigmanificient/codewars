def tower_builder(n_floors):
    return [
        ('*' * (i * 2 + 1)).center((n_floors - 1) * 2 + 1)
        for i in range(n_floors)
    ]


def test_tower_builder():
    assert tower_builder(1), ['*', ]
    assert tower_builder(2), [' * ', '***']
    assert tower_builder(3), ['  *  ', ' *** ', '*' * 5]

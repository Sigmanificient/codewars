"""Kata url: https://www.codewars.com/kata/56576f82ab83ee8268000059."""


def spacey(array):
    return [
        ''.join(array[:i])
        for i in range(1, len(array) + 1)
    ]


def test_spacey():
    assert spacey(['kevin', 'has', 'no', 'space']) == [
        'kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace'
    ]

    assert spacey(['this', 'cheese', 'has', 'no', 'holes']) == [
        'this', 'thischeese', 'thischeesehas',
        'thischeesehasno', 'thischeesehasnoholes'
    ]

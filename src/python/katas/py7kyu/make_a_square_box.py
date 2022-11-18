"""Kata url: https://www.codewars.com/kata/58644e8ddf95f81a38001d8d."""


def box(n):
    return [
        ''.join(
            '-' if {x, y}.intersection({0, n - 1}) else ' '
            for x in range(n)
        ) for y in range(n)
    ]


def test_box():
    assert box(5) == [
        '-----',
        '-   -',
        '-   -',
        '-   -',
        '-----'
    ]

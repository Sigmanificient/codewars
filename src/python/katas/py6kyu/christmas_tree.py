"""Kata url: https://www.codewars.com/kata/52755006cc238fcae70000ed."""


def christmas_tree(height):
    if height == 0:
        return ''

    size = 2 * (height - 1) + 1
    return '\n'.join(
        ('*' * (i * 2 + 1)).center(size)
        for i in range(height)
    )


def test_christmas_tree():
    assert christmas_tree(0) == ''
    assert christmas_tree(1) == '*'
    assert christmas_tree(2) == ' * \n***'
    assert christmas_tree(3) == '  *  \n *** \n*****'
    assert christmas_tree(4) == '   *   \n  ***  \n ***** \n*******'

"""Kata url: https://www.codewars.com/kata/520446778469526ec0000001."""


def same_structure_as(original, other):
    if not isinstance(original, list):
        return not isinstance(other, list)

    if not isinstance(other, list):
        return not isinstance(original, list)

    if len(original) != len(other):
        return False

    for org_item, other_item in zip(original, other):
        if not same_structure_as(org_item, other_item):
            return False

    return True


def test_as_structure_as():
    assert same_structure_as([1, 1, 1], [2, 2, 2])
    assert same_structure_as([1, [1, 1]], [2, [2, 2]])
    assert not same_structure_as([1, [1, 1]], [[2, 2], 2])
    assert not same_structure_as([1, [1, 1]], [2, [2]])

    assert same_structure_as([[[], []]], [[[], []]])
    assert not same_structure_as([[[], []]], [[1, 1]])

    assert same_structure_as([1, [[[1]]]], [2, [[[2]]]])

    assert not same_structure_as([], 1)
    assert not same_structure_as([], {})

    assert same_structure_as([1, '[', ']'], ['[', ']', 1])

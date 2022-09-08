"""Kata url: https://www.codewars.com/kata/57b6f5aadb5b3d0ae3000611."""


def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays:
        return 0

    if None in array_of_arrays:
        return 0

    lengths = list(len(x) for x in array_of_arrays)

    mn = min(lengths)
    if not mn:
        return 0

    mx = max(lengths)

    candidates = set(range(mn, mx + 1))

    for length in lengths:
        candidates.remove(length)

    return min(candidates)


def test_get_length_of_missing_array():
    assert get_length_of_missing_array([[1], [], [4, 5]]) == 0
    assert get_length_of_missing_array([[1], None, [4, 5]]) == 0
    assert get_length_of_missing_array([]) == 0

    assert get_length_of_missing_array(
        [[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]
    ) == 3

    assert get_length_of_missing_array(
        [[5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]
    ) == 2

    assert get_length_of_missing_array(
        [[None], [None, None, None]]
    ) == 2

    assert get_length_of_missing_array(
        [
            ['a', 'a', 'a'],
            ['a', 'a'],
            ['a', 'a', 'a', 'a'],
            ['a'],
            ['a', 'a', 'a', 'a', 'a', 'a']
        ]
    ) == 5


def array_diff(a, b):
    return [item for item in a if item not in b]


def test_array_diff():
    assert array_diff([1, 2], [1]) == [2]
    assert array_diff([1, 2, 2], [1]) == [2, 2]
    assert array_diff([1, 2, 2], [2]) == [1]
    assert array_diff([1, 2, 2], []) == [1, 2, 2]
    assert array_diff([], [1, 2]) == []
    assert array_diff([1, 2, 3], [1, 2]) == [3]

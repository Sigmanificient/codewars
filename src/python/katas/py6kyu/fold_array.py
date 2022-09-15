"""Kata url: https://www.codewars.com/kata/57ea70aa5500adfe8a000110."""


def fold_array(array, runs):
    for _ in range(runs):
        half = (length := len(array)) // 2
        out = [array[-(i + 1)] + array[i] for i in range(half)]

        if length % 2:
            out.append(array[half])

        array = out

    return array


def test_fold_array():
    assert fold_array([1, 2, 3, 4, 5], 1) == [6, 6, 3]
    assert fold_array([1, 2, 3, 4, 5], 2) == [9, 6]
    assert fold_array([1, 2, 3, 4, 5], 3) == [15]
    assert fold_array([-9, 9, -8, 8, 66, 23], 1) == [14, 75, 0]

    assert fold_array([1, 2, 3, 4, 5, 99, 88, 78, 74, 73], 5) == 427
    assert fold_array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 10) == 0

"""Kata url: https://www.codewars.com/kata/5285bf61f8fc1b181700024c."""


def norm_index_test(seq, ind):
    if seq:
        return seq[(ind % len(seq))]


def test_nor_index_test():
    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert norm_index_test(seq, 0) == 0
    assert norm_index_test(seq, 1) == 1
    assert norm_index_test(seq, -1) == 9
    assert norm_index_test(seq, 10) == 0
    assert norm_index_test([], 10) is None

"""Kata url: https://www.codewars.com/kata/56582133c932d8239900002e."""


def most_frequent_item_count(collection):
    if not collection:
        return 0

    return max(map(collection.count, collection))


def test_most_frequent_item_count():
    assert most_frequent_item_count([]) == 0
    assert most_frequent_item_count([3, -1, -1]) == 2
    assert most_frequent_item_count([9]) == 1
    assert most_frequent_item_count(
        [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
    ) == 5

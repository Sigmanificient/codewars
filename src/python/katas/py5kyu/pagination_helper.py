"""Kata url: https://www.codewars.com/kata/515bb423de843ea99400000a."""
import math


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return math.ceil(self.item_count() / self.items_per_page)

    def page_item_count(self, page_index):
        if page_index >= (pages := self.page_count()):
            return -1

        return (
            self.items_per_page
            if (page_index + 1) != pages else
            (self.item_count() % self.items_per_page)
        )

    def page_index(self, item_index):
        if item_index >= self.item_count() or item_index < 0:
            return -1

        return math.floor(item_index / self.items_per_page)


def test_pagination_helper():
    collection = range(1, 25)
    helper = PaginationHelper(collection, 10)
    assert helper.page_count() == 3

    assert helper.page_item_count(1) == 10
    assert helper.page_item_count(2) == 4
    assert helper.page_item_count(3) == -1

    assert helper.page_index(0) == 0
    assert helper.page_index(23) == 2
    assert helper.page_index(24) == -1
    assert helper.page_index(40) == -1
    assert helper.page_index(3) == 0
    assert helper.page_index(-1) == -1
    assert helper.page_index(-23) == -1

    assert helper.page_index(-15) == -1
    assert helper.item_count() == 24

    helper = PaginationHelper([], 10)
    assert helper.page_index(0) == -1

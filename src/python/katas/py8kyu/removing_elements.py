"""Kata url: https://www.codewars.com/kata/5769b3802ae6f8e4890009d2."""

from typing import List, Union


def remove_every_other(
        my_list: List[Union[int, str]]
) -> List[Union[int, str]]:
    return [x for c, x in enumerate(my_list) if not c % 2]


def test_remove_every_other():
    assert remove_every_other(['Hello', 'Goodbye', 'Hello Again']) == ['Hello', 'Hello Again']
    assert remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]
    assert remove_every_other([[1, 2]]) == [[1, 2]]
    assert remove_every_other([['Goodbye'], {'Great': 'Job'}]) == [['Goodbye']]

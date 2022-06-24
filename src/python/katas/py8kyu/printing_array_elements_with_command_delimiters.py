"""Kata url: https://www.codewars.com/kata/56e2f59fb2ed128081001328."""

from typing import List


def print_array(arr: List[int]) -> str:
    return ','.join(map(str, arr))


def test_print_array():
    assert print_array([2]) == "2"
    assert print_array([2, 4, 5, 2]) == "2,4,5,2"
    assert print_array([2, 4, 5, 2]) == "2,4,5,2"
    assert print_array([2.0, 4.2, 5.1, 2.2]) == "2.0,4.2,5.1,2.2"
    assert print_array(["2", "4", "5", "2"]) == "2,4,5,2"
    assert print_array([True, False, False]) == "True,False,False"

    assert print_array(
        ["hello", "this", "is", "an", "array!", "a", "b", "c", "d", "e!"]
    ) == "hello,this,is,an,array!,a,b,c,d,e!"

    assert print_array(
        [["hello", "this", "is", "an", "array!"], [1, 2, 3, 4, 5]]
    ) == "['hello', 'this', 'is', 'an', 'array!'],[1, 2, 3, 4, 5]"

from typing import List, Optional


def comp(array1: Optional[List[int]], array2: Optional[List[int]]) -> bool:
    """ https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

    Given two arrays a and b write a function comp(a, b) (or compSame(a, b)) that checks whether the two arrays have the
    "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a
    squared, regardless of the order.
    """

    if array1 is None or array2 is None:
        return False

    if len(array1) != len(array2):
        return False

    return all(i * i == j for i, j in zip(sorted(array1, key=abs), sorted(array2)))

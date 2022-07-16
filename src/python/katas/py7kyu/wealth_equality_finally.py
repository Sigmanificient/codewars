"""Kata url: https://www.codewars.com/kata/5815f7e789063238b30001aa."""
from typing import List


def redistribute_wealth(wealth: List[int]) -> List[float]:
    nb_citizen = len(wealth)
    redistributed = sum(wealth) / nb_citizen
    wealth.clear()
    wealth.extend([redistributed] * nb_citizen)


def test_redistribute_wealth():
    # already equal
    wealth_equal = [5, 5, 5, 5, 5]
    assert redistribute_wealth(wealth_equal) is None
    assert wealth_equal == [5, 5, 5, 5, 5]

    wealth_unequal = [0, 10]
    assert redistribute_wealth(wealth_unequal) is None
    assert wealth_unequal == [5, 5]

    # single citizen
    wealth_single = [5]
    assert redistribute_wealth(wealth_single) is None
    assert wealth_single == [5]

    wealth_float = [3, 2, 2]
    assert redistribute_wealth(wealth_float) is None
    assert wealth_float == [2.3333333333333335, 2.3333333333333335, 2.3333333333333335]

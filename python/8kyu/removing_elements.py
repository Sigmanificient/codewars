from typing import List, Union


def remove_every_other(my_list: List[Union[int, str]]) -> List[Union[int, str]]:
    """Kata url: https://www.codewars.com/kata/5769b3802ae6f8e4890009d2."""
    return [x for c, x in enumerate(my_list) if not c % 2]

from typing import List, Any


def filter_list(collection: List[Any]) -> List[int]:
    """Kate url: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd."""
    return [x for x in collection if isinstance(x, int)]

from collections import defaultdict
from typing import Dict, List


def merge(*dicts: Dict[str, int]) -> Dict[str, List[int]]:
    out = defaultdict(list)

    for d in dicts:
        for k, v in d.items():
            out[k].append(v)

    return dict(out)


def test_merge():
    assert merge({}, {}, {}) == {}
    assert merge({"A": 1, "B": 2, "C": 3}) == {"A": [1], "B": [2], "C": [3]}

    assert merge({"A": 1}, {"B": 2}) == {"A": [1], "B": [2]}
    assert (
        merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5})
        == {"A": [1, 4], "B": [2], "C": [3], "D": [5]}
    )

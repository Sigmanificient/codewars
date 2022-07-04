from typing import List, Any


def alternate(n: int, a: List[Any], b: List[Any]) -> List[Any]:
    return [b if c % 2 else a for c in range(n)]


def test_alternate():
    assert alternate(0, "lemons", "apples") == []
    assert alternate(5, True, False) == [True, False, True, False, True]
    assert alternate(20, "blue", "red") == [
        'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red',
        'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red',
        'blue', 'red', 'blue', 'red'
    ]

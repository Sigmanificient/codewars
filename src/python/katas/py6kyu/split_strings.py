from typing import List


def solution(s: str) -> List[str]:
    return [s[i:i + 2].ljust(2, '_') for i in range(0, len(s), 2)]


def test_solution():
    assert solution("") == []
    assert solution("x") == ["x_"]
    assert solution("ab") == ["ab"]

    assert solution("asdfads") == ['as', 'df', 'ad', 's_']
    assert solution("asdfadsf") == ['as', 'df', 'ad', 'sf']

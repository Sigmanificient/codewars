"""Kata url: https://www.codewars.com/kata/51c7d8268a35b6b8b40002f2."""


def solution(pairs):
    return ','.join(
        f"{k} = {v}"
        for k, v in sorted(
            pairs.items(), key=lambda x: ord(str(x[0]))
        )
    )


def test_solution():
    assert solution({}) == ''
    assert solution({'a': 1, 'b': 2}) == 'a = 1,b = 2'
    assert solution({'a': 'b', 'b': 'a'}) == 'a = b,b = a'
    assert solution({0: 'a', 'b': 2}) == '0 = a,b = 2'
    assert solution({'b': 1, 'c': 2, 'e': 3}) == 'b = 1,c = 2,e = 3'

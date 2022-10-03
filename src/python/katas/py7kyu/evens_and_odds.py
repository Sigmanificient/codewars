"""Kata url: https://www.codewars.com/kata/583ade15666df5a64e000058."""


def evens_and_odds(n: int) -> str:
    return f"{n:{'x' if n % 2 else 'b'}}"


def test_even_and_odds():
    assert evens_and_odds(2) == '10'
    assert evens_and_odds(0) == '0'
    assert evens_and_odds(13) == 'd'
    assert evens_and_odds(47) == '2f'
    assert evens_and_odds(12800) == '11001000000000'
    assert evens_and_odds(8172381723) == '1e71ca61b'

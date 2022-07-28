"""Kata url: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9."""


def find_short(s: str) -> int:
    return len(sorted(s.split(), key=len)[0])


def test_find_short():
    assert find_short(
        "bitcoin take over the world maybe who knows perhaps"
    ) == 3

    assert find_short(
        "turns out random test cases are easier than writing out basic ones"
    ) == 3

    assert find_short(
        "lets talk about javascript the best language"
    ) == 3

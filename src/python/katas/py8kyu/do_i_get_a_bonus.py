"""Kata url: https://www.codewars.com/kata/56f6ad906b88de513f000d96."""


def bonus_time(salary: int, bonus: bool) -> str:
    return f"${salary * 10 if bonus else salary}"


def test_bonus_time():
    assert bonus_time(2, True) == "$20"
    assert bonus_time(78, False) == "$78"
    assert bonus_time(67890, True) == "$678900"

    assert bonus_time(10000, True) == "$100000"
    assert bonus_time(25000, True) == "$250000"
    assert bonus_time(10000, False) == "$10000"
    assert bonus_time(60000, False) == "$60000"

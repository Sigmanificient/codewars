"""Kata url: https://www.codewars.com/kata/56f6ad906b88de513f000d96."""


def bonus_time(salary: int, bonus: bool) -> str:
    return f"${salary * 10 if bonus else salary}"
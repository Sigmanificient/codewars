"""Kata url: https://www.codewars.com/kata/58528e9e22555d8d33000163."""
from datetime import datetime


def minutes_to_midnight(d: datetime) -> str:
    progress = (d.hour * 3600 + d.minute * 60 + d.second)
    return f'{(86400 - progress) / 60:.0f} minutes'


def test_minutes_to_midnight():
    today = datetime.now()

    d = datetime(today.year, today.month, today.day, 23, 22, 31)
    assert minutes_to_midnight(d) == "37 minutes"

    d = datetime(today.year, today.month, today.day, 12, 15, 29)
    assert minutes_to_midnight(d) == "705 minutes"

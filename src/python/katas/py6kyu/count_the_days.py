"""Kata url: https://www.codewars.com/kata/5837fd7d44ff282acd000157."""
from datetime import datetime


def count_days(d):
    elapsed = (d - datetime.now()).total_seconds()
    days = round(elapsed / 86400)

    if abs(days) < 1:
        return 'Today is the day!'

    return 'The day is in the past!' if days < 0 else f'{days} days'


def test_count_days():
    import re
    from time import time

    assert count_days(
        datetime(2016, 12, 24, 18, 0)
    ) == "The day is in the past!"

    assert count_days(datetime.now()) == 'Today is the day!'

    d = datetime.now()
    assert re.fullmatch(
        '36[456] days',
        count_days(
            datetime(d.year + 1, d.month, d.day)
        )
    )

    stamp = time()

    assert count_days(
        datetime.fromtimestamp(stamp + 90000)
    ) == '1 days'

    assert count_days(
        datetime.fromtimestamp(stamp + 86400 * 42)
    ) == '42 days'

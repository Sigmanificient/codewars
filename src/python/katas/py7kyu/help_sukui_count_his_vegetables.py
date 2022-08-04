"""Kata url: https://www.codewars.com/kata/56ff1667cc08cacf4b00171b."""
from collections import Counter
from typing import List, Tuple

VEGETABLES = [
    "cabbage",
    "carrot",
    "celery",
    "cucumber",
    "mushroom",
    "onion",
    "pepper",
    "potato",
    "tofu",
    "turnip",
]


def count_vegetables(string: str) -> List[Tuple[int, str]]:
    return sorted(
        [(v, k) for k, v in Counter(string.split()).items() if k in VEGETABLES],
        reverse=True,
    )


def test_count_vegetables():
    assert count_vegetables(
        'potato tofu cucumber cabbage turnip pepper onion carrot celery '
        'mushroom potato tofu cucumber cabbage'
    ) == [
        (2, 'tofu'), (2, 'potato'), (2, 'cucumber'), (2, 'cabbage'),
        (1, 'turnip'), (1, 'pepper'), (1, 'onion'), (1, 'mushroom'),
        (1, 'celery'), (1, 'carrot')
    ]

    assert count_vegetables(
        'mushroom chopsticks chopsticks turnip mushroom carrot mushroom cabbage '
        'mushroom carrot tofu pepper cabbage potato cucumber mushroom mushroom '
        'mushroom potato turnip chopsticks cabbage celery celery turnip pepper '
        'chopsticks potato potato onion cabbage cucumber onion pepper onion '
        'cabbage potato tofu carrot cabbage cabbage turnip mushroom cabbage '
        'cabbage cucumber cabbage chopsticks turnip pepper onion pepper onion '
        'mushroom turnip carrot carrot tofu onion tofu chopsticks chopsticks '
        'chopsticks mushroom cucumber chopsticks carrot potato cabbage cabbage '
        'carrot mushroom chopsticks mushroom celery turnip onion carrot turnip '
        'cucumber carrot potato mushroom turnip mushroom cabbage tofu turnip '
        'turnip turnip mushroom tofu potato pepper turnip potato turnip celery '
        'carrot turnip'
    ) == [
        (15, 'turnip'), (15, 'mushroom'), (13, 'cabbage'), (10, 'carrot'),
        (9, 'potato'), (7, 'onion'), (6, 'tofu'), (6, 'pepper'),
        (5, 'cucumber'), (4, 'celery')
    ]

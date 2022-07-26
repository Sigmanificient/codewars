"""Kata url: https://www.codewars.com/kata/59bd5dc270a3b7350c00008b."""

from typing import List


def check_the_bucket(bucket: List[str]) -> bool:
    return "gold" in bucket


def test_check_the_bucket():
    assert check_the_bucket(
        [
            "stone",
            "stone",
            "gold",
            "stone",
            "stone",
        ]
    )
    assert not check_the_bucket(
        [
            "stone",
            "stone",
            "stone",
            "stone",
            "stone",
        ]
    )
    assert check_the_bucket(
        [
            "gold",
            "gold",
            "gold",
            "gold",
            "gold",
        ]
    )

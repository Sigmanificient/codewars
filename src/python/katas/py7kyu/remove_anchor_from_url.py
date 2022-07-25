"""Kata url: https://www.codewars.com/kata/51f2b4448cadf20ed0000386."""
import re


def remove_url_anchor(url: str) -> str:
    return re.match(r'[^#]*', url)[0]


def test_remove_url_anchor():
    assert remove_url_anchor(
        "www.codewars.com#about"
    ) == "www.codewars.com"

    assert remove_url_anchor(
        "www.codewars.com/katas/?page=1#about"
    ) == "www.codewars.com/katas/?page=1"

    assert remove_url_anchor(
        "www.codewars.com/katas/"
    ) == "www.codewars.com/katas/"

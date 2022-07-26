"""Kata url: https://www.codewars.com/kata/514a024011ea4fb54200004b."""
import re


def domain_name(url):
    return re.search(r"^(https?:)?(\.|/+)?(www\.)?(?P<d>[^./]*)\.", url)["d"]


def test_domain_name():
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name(r"https://youtube.com") == "youtube"

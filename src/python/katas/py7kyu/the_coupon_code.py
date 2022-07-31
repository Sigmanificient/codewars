"""Kata url: https://www.codewars.com/kata/539de388a540db7fec000642."""
from datetime import datetime
from typing import Union


def _to_date(d: str) -> datetime:
    return datetime.strptime(d, "%B %d, %Y")


def check_coupon(
    entered_code: Union[str, int, bool],
    correct_code: Union[str, int, bool],
    current_date: str,
    expiration_date: str,
):
    return (
        entered_code == correct_code
        and isinstance(entered_code, type(correct_code))
        and _to_date(current_date) <= _to_date(expiration_date)
    )


def test_check_coupon():
    assert check_coupon("123", "123", "September 5, 2014", "October 1, 2014")
    assert check_coupon("a12v564", "a12v564", "March 5, 1998", "March 25, 1998")
    assert check_coupon("123ablqc0", "123ablqc0", "July 5, 2000", "July 5, 2000")
    assert check_coupon("0a12bc64", "0a12bc64", "March 6, 2005", "March 5, 2006")
    assert check_coupon("abc", "abc", "November 8, 2013", "November 5, 2014")

    assert not check_coupon("123a", "123", "September 5, 2014", "October 1, 2014")
    assert not check_coupon("12abcd3", "12abcd3", "January 5, 2014", "January 1, 2014")
    assert not check_coupon(0, False, "September 5, 2014", "September 25, 2014")
    assert not check_coupon("0", False, "September 5, 2014", "September 25, 2014")
    assert not check_coupon("1", True, "September 5, 2014", "September 25, 2014")
    assert not check_coupon(1 + 1, "2", "September 5, 2014", "September 25, 2014")

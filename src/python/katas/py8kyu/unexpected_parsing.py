"""Kata url: https://www.codewars.com/kata/54fdaa4a50f167b5c000005f."""


def get_status(is_busy):
    return {'status': "busy" if is_busy else "available"}


def test_get_status():
    assert get_status(True)["status"], "busy"
    assert get_status(False)["status"], "available"

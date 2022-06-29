import re


def validate_pin(pin: str) -> bool:
    return re.fullmatch(r'^\d{4}$|^\d{6}$', pin) is not None


def test_validate_pin():
    assert not validate_pin("1")
    assert not validate_pin("12")
    assert not validate_pin("123")
    assert not validate_pin("12345")
    assert not validate_pin("1234567")
    assert not validate_pin("-1234")
    assert not validate_pin("-12345")
    assert not validate_pin("1.234")
    assert not validate_pin("00000000")

    assert not validate_pin("a234")
    assert not validate_pin(".234")

    assert validate_pin("1234")
    assert validate_pin("0000")
    assert validate_pin("1111")
    assert validate_pin("123456")
    assert validate_pin("098765")
    assert validate_pin("000000")
    assert validate_pin("123456")
    assert validate_pin("090909")

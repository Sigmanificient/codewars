"""Kata url: https://www.codewars.com/kata/515decfd9dcfc23bb6000006."""


def is_valid_IP(string: str) -> bool:
    if string.count(".") != 3:
        return False

    digits = string.split(".")

    if not "".join(digits).isdigit():
        return False

    if any(int(n) > 255 for n in digits):
        return False

    if any(int(n) > 0 and n.startswith("0") for n in digits):
        return False

    return True


def test_ips():
    assert is_valid_IP("12.255.56.1")
    assert is_valid_IP("127.1.1.0")
    assert is_valid_IP("0.0.0.0")
    assert is_valid_IP("0.34.82.53")
    assert not is_valid_IP("192.168.1.300")

    assert not is_valid_IP("")
    assert not is_valid_IP("abc.def.ghi.jkl")
    assert not is_valid_IP("123.456.789.0")
    assert not is_valid_IP("12.34.56")
    assert not is_valid_IP("12.34.56 .1")
    assert not is_valid_IP("12.34.56.-1")
    assert not is_valid_IP("123.045.067.089")

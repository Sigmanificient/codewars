"""Kata url: https://www.codewars.com/kata/515decfd9dcfc23bb6000006."""


def is_valid_IP(string: str) -> bool:
    if string.count('.') != 3:
        return False

    digits = string.split('.')

    if not ''.join(digits).isdigit():
        return False

    if any(
        int(n) > 255 for n in digits
    ):
        return False

    if any(
        int(n) > 0 and n.startswith('0') for n in digits
    ):
        return False

    return True

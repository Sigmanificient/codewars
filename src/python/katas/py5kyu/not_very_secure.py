import string


def alphanumeric(password: str) -> bool:
    return len(password) > 0 and all(
        x.lower() in string.ascii_lowercase + string.digits
        for x in password
    )


def test_alphanumeric():
    assert not alphanumeric('')
    assert not alphanumeric(' ' * 5)

    assert alphanumeric('abc')
    assert alphanumeric('abc123')
    assert not alphanumeric('abc123%')
    assert not alphanumeric('abc123@')

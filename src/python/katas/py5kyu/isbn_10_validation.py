"""Kata url: https://www.codewars.com/kata/51fc12de24a9d8cb0e000001."""


def valid_ISBN10(isbn: str) -> bool:
    if len(isbn) != 10:
        return False

    if not isbn[:-1].isdigit():
        return False

    if not (isbn[-1].isdigit() or isbn[-1] == 'X'):
        return False

    return not sum(
        int(x, 16) * (c + 1) for c, x in enumerate(
            isbn.replace('X', 'a')
        )
    ) % 11


def test_valid_isbn():
    assert valid_ISBN10('1112223339')
    assert valid_ISBN10('048665088X')
    assert valid_ISBN10('1293000000')
    assert valid_ISBN10('1234554321')

    assert not valid_ISBN10('1293')
    assert not valid_ISBN10('1234512345')
    assert not valid_ISBN10('X123456788')
    assert not valid_ISBN10('ABCDEFGHIJ')
    assert not valid_ISBN10('XXXXXXXXXX')
    assert not valid_ISBN10('123456789T')

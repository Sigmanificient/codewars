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
    )

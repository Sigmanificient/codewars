"""Kata url: https://www.codewars.com/kata/58ae6ae22c3aaafc58000079."""


def permute_a_palindrome(word: str) -> bool:
    counts = [word.count(c) for c in set(word)]
    max_odd = len(word) % 2

    for count in counts:
        odd = count % 2
        if not odd:
            continue

        if not max_odd:
            return False

        max_odd -= 1

    return True


def test_permute_a_palindrome():
    assert permute_a_palindrome("a")
    assert permute_a_palindrome("aa")
    assert permute_a_palindrome("baa")
    assert permute_a_palindrome("aab")
    assert not permute_a_palindrome("baabcd")
    assert not permute_a_palindrome("racecars")

    assert not permute_a_palindrome("abcdefghba")
    assert permute_a_palindrome("")

"""Kata url: https://www.codewars.com/kata/587f0abdd8730aafd4000035."""

import hashlib
from itertools import permutations


def sha256_cracker(hash_, chars):
    for letters in permutations(chars):
        word = "".join(letters)

        if hashlib.sha256(word.encode()).hexdigest() == hash_:
            return word

    return None


def test_sha256_cracker():
    assert (
        sha256_cracker(
            "b8c49d81cb795985c007d78379e98613a4dfc824381be472238dbd2f974e37ae",
            "deGioOstu",
        )
        == "GoOutside"
    )

    assert (
        sha256_cracker(
            "f58262c8005bb64b8f99ec6083faf050c502d099d9929ae37ffed2fe1bb954fb", "abc"
        )
        is None
    )

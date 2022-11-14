"""Kata url: https://www.codewars.com/kata/5bc7bb444be9774f100000c3."""
import pytest


class VersionManager:
    def __init__(self, version=""):
        if not version:
            version = '0.0.1'

        major, minor, patch, *_ = (version + '.0.0').split('.')

        if not all(map(str.isdigit, (major, minor, patch))):
            raise ValueError('Error occurred while parsing version!')

        self.__major = int(major)
        self.__minor = int(minor)
        self.__patch = int(patch)

        self.__versions = []

    def __keep_versions(self):
        self.__versions.append(
            (self.__major, self.__minor, self.__patch)
        )

    def major(self):
        self.__keep_versions()
        self.__major += 1
        self.__minor = 0
        self.__patch = 0
        return self

    def minor(self):
        self.__keep_versions()
        self.__minor += 1
        self.__patch = 0
        return self

    def patch(self):
        self.__keep_versions()
        self.__patch += 1
        return self

    def rollback(self):
        if not self.__versions:
            raise ValueError("Cannot rollback!")

        self.__major, self.__minor, self.__patch = self.__versions.pop()
        return self

    def release(self):
        return f"{self.__major}.{self.__minor}.{self.__patch}"


def test_version_manager():

    assert VersionManager().release() == "0.0.1"
    assert VersionManager("").release() == "0.0.1"

    assert VersionManager("1.2.3").release() == "1.2.3"
    assert VersionManager("1.2.3.4").release() == "1.2.3"
    assert VersionManager("1.2.3.d").release() == "1.2.3"

    assert VersionManager("1").release() == "1.0.0"
    assert VersionManager("1.1").release() == "1.1.0"

    assert VersionManager().major().release() == "1.0.0"
    assert VersionManager("1.2.3").major().release() == "2.0.0"
    assert VersionManager("1.2.3").major().major().release() == "3.0.0"

    assert VersionManager().minor().release() == "0.1.0"
    assert VersionManager("1.2.3").minor().release() == "1.3.0"

    assert VersionManager("1").minor().release() == "1.1.0"
    assert VersionManager("4").minor().minor().release() == "4.2.0"

    assert VersionManager().patch().release() == "0.0.2"
    assert VersionManager("1.2.3").patch().release() == "1.2.4"
    assert VersionManager("4").patch().patch().release() == "4.0.2"

    assert VersionManager().major().rollback().release() == "0.0.1"
    assert VersionManager().minor().rollback().release() == "0.0.1"
    assert VersionManager().patch().rollback().release() == "0.0.1"
    assert VersionManager().major().patch().rollback().release() == "1.0.0"
    assert (
        VersionManager().major().patch()
        .rollback().major().rollback().release() == "1.0.0"
    )

    m = VersionManager("1.2.3")
    m.major()
    m.minor()
    assert m.release() == "2.1.0"

    with pytest.raises(ValueError):
        VersionManager("a.b.c")

    with pytest.raises(ValueError):
        VersionManager().rollback()

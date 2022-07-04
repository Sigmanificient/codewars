"""Kata url: https://www.codewars.com/kata/6089c7992df556001253ba7d."""

from typing import List, Set


class Song:

    def __init__(self, title: str, artist: str):
        self.title: str = title
        self.artist: str = artist
        self.listeners: List[str] = []

    def how_many(self, peoples):
        peoples: Set[str] = {p.lower() for p in peoples}
        new_l: List[str] = [p for p in peoples if p not in self.listeners]
        self.listeners.extend(tuple(new_l))
        return len(new_l)


def test_solution():
    mount_moose = Song("Mount Moose", "The Snazzy Moose")
    assert mount_moose.title == 'Mount Moose'
    assert mount_moose.artist == 'The Snazzy Moose'
    assert mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn']) == 5
    assert mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']) == 2
    assert mount_moose.how_many(['Amanda', 'CalEb', 'CarL', 'Furgus']) == 2
    assert mount_moose.how_many(['JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE']) == 1

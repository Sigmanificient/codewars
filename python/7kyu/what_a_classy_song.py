from typing import List, Set


class Song:
    """Kata url: https://www.codewars.com/kata/6089c7992df556001253ba7d."""

    def __init__(self, title: str, artist: str):
        self.title: str = title
        self.artist: str = artist
        self.listeners: List[str] = []

    def how_many(self, peoples):
        peoples: Set[str] = {p.lower() for p in peoples}
        new_l: List[str] = [p for p in peoples if p not in self.listeners]
        self.listeners.extend(tuple(new_l))
        return len(new_l)

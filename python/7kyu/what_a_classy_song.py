class Song:
    """Kata url: https://www.codewars.com/kata/6089c7992df556001253ba7d."""

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = []

    def how_many(self, peoples):
        peoples = {p.lower() for p in peoples}
        new_l = [p for p in peoples if p not in self.listeners]
        self.listeners.extend(tuple(new_l))
        return len(new_l)

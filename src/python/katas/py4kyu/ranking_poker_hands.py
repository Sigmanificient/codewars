"""Kara url: https://www.codewars.com/kata/5739174624fc28e188000465."""

from collections import Counter

RESULT = ["Loss", "Tie", "Win"]

CARDS = "..23456789TJQKA"
CARDS_COUNT = len(CARDS)


class Card:

    def __init__(self, value):
        self.rank = CARDS.index(value[0])
        self.suit = value[1]

    def __eq__(self, other):
        return self.rank == other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __hash__(self):
        return self.rank


class PokerHand:

    def __init__(self, hand):
        self.cards = list(sorted(map(Card, hand.split(" "))))

        is_flush = len(set(card.suit for card in self.cards)) == 1

        groups = {
            k: c for k, c in Counter(card for card in self.cards).items()
            if c > 1
        }
        counts = Counter(groups.values())

        is_straight = all(
            (card_a.rank + 1) == card_b.rank
            for card_a, card_b in zip(self.cards, self.cards[1::])
        ) or all(
            card.rank == rank
            for card, rank in zip(self.cards, (2,3,4,5,CARDS_COUNT-1))
        )

        self.level = 0
        for i, (crit_flush, crit_counts, crit_straight) in enumerate((
            (False, {}, False), # High cards
            (False, {2: 1}, False), # Pair
            (False, {2: 2}, False), # Two pairs
            (False, {3: 1}, False), # Three of a kind
            (False, {}, True), # Straight
            (True, {}, False), # Flush
            (False, {2: 1, 3: 1}, False), # Full house
            (False, {4: 1}, False), # Four of a kind
            (True, {}, True), # Straight flush
        ), start=1):
            if (
                crit_flush == is_flush
                and counts == Counter(crit_counts)
                and crit_straight == is_straight
            ):
                self.level = i

        self.score = (
            ((CARDS_COUNT ** 8) * self.level)
            + sum(
                sorted(
                    card.rank * (CARDS_COUNT ** i)
                    for i, card in enumerate(self.cards)
                    if card not in groups)
                )
            + sum(
                k.rank * ((CARDS_COUNT ** (6 + i)))
                for i, (k, c) in enumerate(sorted(groups.items()))
            )
        )

    def compare_with(self, other):
        diff = self.score - other.score
        return RESULT[(diff == 0) - (diff > 0)]
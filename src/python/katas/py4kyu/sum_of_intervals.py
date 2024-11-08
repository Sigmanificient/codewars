"""Kata url: https://www.codewars.com/kata/52b7ed099cdc285c300001cd."""

from __future__ import annotations
from dataclasses import dataclass
from typing import MutableSequence

IntervalTuple = tuple[int, int]
Split = tuple[IntervalTuple, IntervalTuple]


@dataclass
class Interval:
    lo: int
    hi: int

    def reduce(self, other: Interval) -> Split | None:
        if self.lo < other.lo and self.hi > other.hi:
            return (self.lo, other.lo), (other.hi, self.hi)

        if self.hi >= other.lo and self.hi <= other.hi:
            self.hi = other.lo
        if self.lo <= other.hi and self.lo >= other.lo:
            self.lo = other.hi

        if self.hi < self.lo or self.lo > self.hi:
            self.lo = self.hi

    def tuple(self) -> IntervalTuple:
        return (self.lo, self.hi)
            
    def sum(self) -> int:
        if self.lo > 0 or self.hi <= 0:
            return self.hi - self.lo
        else:
            return -self.lo + self.hi


def sum_of_intervals(intervals: MutableSequence[IntervalTuple]):
    s = c = 0
    
    while c < len(intervals):
        current = intervals[c]
        iv = Interval(*current)

        splitted = None
        for reduce in intervals[:c]:
            splitted = iv.reduce(Interval(*reduce))
            if splitted is not None:
                break
        else:
            s += iv.sum()
            c += 1
        
        if splitted is not None:
            a, b = splitted
            intervals[c] = a
            intervals.append(b)

    return s
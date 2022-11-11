"""Kata url: https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa."""


class Stack:

    def __init__(self, string):
        self.__stack = string
        self.__len = len(self.__stack)
        self.i = 0

    @property
    def top(self):
        if self.i >= self.__len:
            raise None
        return self.__stack[self.i]

    def get_rem(self, skip=0):
        return self.__stack[self.i + skip:]

    def pop(self):
        self.i += 1


def is_merge(s, part1, part2):
    if (len(part1) + len(part2)) != len(s):
        return False

    left = Stack(part1)
    right = Stack(part2)

    for c, char in enumerate(s):
        if char == left.top == right.top:
            return (
                is_merge(s[c + 1:], left.get_rem(), right.get_rem(1))
                or is_merge(s[c + 1:], left.get_rem(1), right.get_rem())
            )

        if char == left.top:
            left.pop()
            continue

        if char == right.top:
            right.pop()
            continue

        return False
    return True

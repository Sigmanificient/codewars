"""Kata url: https://www.codewars.com/kata/55f89832ac9a66518f000118."""
from __future__ import annotations

from collections import defaultdict
from enum import Enum
from io import StringIO
from typing import List, Tuple, Dict


class Sign(Enum):
    POSITIVE = 0
    NEGATIVE = 1

    @classmethod
    def from_count(cls, minus_count: int) -> Sign:
        return cls(minus_count & 1)

    def to_multiplier(self) -> int:
        return 1 if self.value == 0 else -1

    def __repr__(self) -> str:
        return '-' if self.value == 1 else '+'


class Parser:

    def __init__(self, expression: str):
        self.expr = expression
        self.__expr_len = len(expression)
        self.__i = 0

    @property
    def cursor(self) -> str:
        if self.__i >= self.__expr_len:
            return ''

        return self.expr[self.__i]

    def advance_cursor(self):
        self.__i += 1

    def eat_integer(self) -> int:
        digits = ''

        while self.cursor.isdigit():
            digits += self.cursor
            self.advance_cursor()

        return int(digits or '1')

    def eat_symbol(self) -> str:
        symbol = ''

        while self.cursor.isalpha():
            symbol += self.cursor
            self.advance_cursor()

        return ''.join(sorted(symbol))

    def eat_sign(self) -> Sign:
        minus_count = 0

        while self.cursor in '-+':
            minus_count += self.cursor == '-'
            self.advance_cursor()

        return Sign.from_count(minus_count)

    def parse_terms(self) -> List[Tuple[Sign, int, str]]:
        parsed = []

        while self.cursor:
            parsed.append(
                (
                    self.eat_sign(),
                    self.eat_integer(),
                    self.eat_symbol()
                )
            )

        return parsed


def format_polynomial(monomials: Dict[str, int]) -> str:
    longest_monomials = len(max(monomials.keys(), key=len))
    first_term = True
    buf = StringIO()

    for mono, val in sorted(
        monomials.items(),
        key=lambda kv: kv[0].rjust(longest_monomials, '_')
    ):
        if not val:
            continue
        if not first_term and val > 0:
            buf.write('+')
        elif val < 0:
            buf.write('-')
        if val not in (-1, 1):
            buf.write(str(abs(val)))
        buf.write(mono)
        first_term = False
    return buf.getvalue()


def simplify(poly: str) -> str:
    parser = Parser(poly)
    terms = parser.parse_terms()

    monomials = defaultdict(int)
    for sign, num, mono in terms:
        monomials[mono] += num * sign.to_multiplier()

    return format_polynomial(monomials)


def test_simplify():
    assert simplify("dc+dcba") == "cd+abcd"
    assert simplify("-a+5ab+3a-c-2a") == "-c+5ab"
    assert simplify("-abc+3a+2ac") == "3a+2ac-abc"
    assert simplify("xyz-xz") == "-xz+xyz"
    assert simplify("a+ca-ab") == "a-ab+ac"
    assert simplify("xzy+zby") == "byz+xyz"
    assert simplify("-y+x") == "x-y"
    assert simplify("y-x") == "-x+y"

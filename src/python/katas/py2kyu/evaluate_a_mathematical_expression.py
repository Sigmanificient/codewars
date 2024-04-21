"""Kata url: https://www.codewars.com/kata/52a78825cdfc2cfc87000005."""
from enum import Enum

import pytest


class TokenType(Enum):
    INTEGER = 0
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4
    LEFT_PARENTHESIS = 5
    RIGHT_PARENTHESIS = 6
    MINUS = 7
    END_OF_FILE = 8


class Token:

    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f'Token({self.type.name}, {self.value})'


class InvalidCharacter(Exception):
    pass


class InvalidSyntax(Exception):
    pass


class Lexer:

    def __init__(self, string):
        self.string = string
        self.pos = 0

        self.current_char = self.string[self.pos]
        self.previous_char = ''

        self.char_tokens = {
            '+': TokenType.ADDITION,
            '-': TokenType.SUBTRACTION,
            '*': TokenType.MULTIPLICATION,
            '/': TokenType.DIVISION,
            '(': TokenType.LEFT_PARENTHESIS,
            ')': TokenType.RIGHT_PARENTHESIS
        }

    def advance(self):
        self.previous_char = self.current_char
        self.pos += 1

        if self.pos <= len(self.string) - 1:
            self.current_char = self.string[self.pos]
            return

        self.current_char = None

    def skip_whitespace(self):
        previous_char = self.previous_char

        while (
                self.current_char is not None
                and self.current_char.isspace()
        ):
            self.advance()

        if self.previous_char != previous_char:
            self.previous_char = previous_char

    def integer(self):
        digits = ''

        if self.current_char == '-':
            self.advance()
            digits += '-'

        self.skip_whitespace()

        while (
                self.current_char is not None
                and self.current_char.isdigit()
        ):
            digits += self.current_char
            self.advance()

        if not digits or digits == '-' or digits.count('-') > 1:
            raise InvalidSyntax(f'{digits}')

        return digits

    def get_next_token(self):
        if self.current_char is None:
            return Token(TokenType.END_OF_FILE)

        self.skip_whitespace()
        if (
            self.current_char == '-'
            and self.previous_char is not None
            and self.previous_char in '+-*/('
        ):
            self.advance()
            return Token(TokenType.MINUS, self.previous_char)

        if self.current_char.isdigit():
            return Token(TokenType.INTEGER, self.integer())

        token = self.char_tokens.get(self.current_char)
        if token is None:
            raise InvalidCharacter(self.current_char)

        self.advance()
        return Token(token, self.previous_char)



class AST:
    pass


class UnaryOp(AST):

    def __init__(self, token, next_):
        self.token = token
        self.next = next_


class BinOp(AST):

    def __init__(self, left, token, right):
        self.left = left
        self.token = token
        self.right = right


class Num(AST):

    def __init__(self, token):
        self.token = token

    @property
    def value(self):
        return int(self.token.value)


class Parser:

    def __init__(self, lexer):
        self.lexer = lexer

        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type != token_type:
            raise InvalidSyntax(f'Expected {token_type.name}')

        self.current_token = self.lexer.get_next_token()

    def factor(self):
        token = self.current_token

        if token.type == TokenType.INTEGER:
            self.eat(TokenType.INTEGER)
            return Num(token)

        if token.type == TokenType.LEFT_PARENTHESIS:
            self.eat(TokenType.LEFT_PARENTHESIS)
            node = self.expr()
            self.eat(TokenType.RIGHT_PARENTHESIS)
            return node

        if token.type == TokenType.MINUS:
            self.eat(TokenType.MINUS)
            node = self.factor()
            return UnaryOp(TokenType.MINUS, node)

        raise InvalidSyntax(
            f'Expected INTEGER or LEFT_PARENTHESIS, got {token}'
        )

    def term(self):
        node = self.factor()

        while self.current_token.type in (
            TokenType.MULTIPLICATION,
            TokenType.DIVISION
        ):
            token = self.current_token
            if token.type == TokenType.MULTIPLICATION:
                self.eat(TokenType.MULTIPLICATION)

            elif token.type == TokenType.DIVISION:
                self.eat(TokenType.DIVISION)

            node = BinOp(node, token, self.factor())

        return node

    def expr(self):
        node = self.term()

        while self.current_token.type in (
            TokenType.ADDITION,
            TokenType.SUBTRACTION,
            TokenType.MINUS
        ):
            token = self.current_token
            if token.type == TokenType.ADDITION:
                self.eat(TokenType.ADDITION)

            elif token.type == TokenType.SUBTRACTION:
                self.eat(TokenType.SUBTRACTION)

            node = BinOp(node, token, self.term())

        return node

    parse = expr


class Interpreter:

    def __init__(self, parser):
        self.parser = parser
        self.visit_methods = {
            Num: self.visit_num,
            BinOp: self.visit_bin_op,
            UnaryOp: self.visit_unary_op,
        }

    def visit(self, node) -> int:
        visit_method = self.visit_methods.get(node.__class__)

        if visit_method is None:
            raise TypeError(f'No visit method for {node.__class__}')

        return visit_method(node)

    @staticmethod
    def visit_num(node):
        return node.value

    def visit_unary_op(self, node):
        return -self.visit(node.next)

    def visit_bin_op(self, node):
        ops = {
            TokenType.ADDITION: lambda x, y: x + y,
            TokenType.SUBTRACTION: lambda x, y: x - y,
            TokenType.MULTIPLICATION: lambda x, y: x * y,
            TokenType.DIVISION: lambda x, y: x / y
        }

        op = ops[node.token.type]
        return op(
            self.visit(node.left),
            self.visit(node.right)
        )

    def interpret(self) -> int | float:
        tree = self.parser.parse()
        return self.visit(tree)


def calc(expression) -> int | float:
    lexer = Lexer(expression)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)

    return interpreter.interpret()


def test_calc():
    assert calc('1 + 1') == 2
    assert (calc('8/16') - 0.5) < 0.0001
    assert calc('3 -(-1)') == 4
    assert calc('2 + -2') == 0
    assert calc('10- 2- -5') == 13
    assert calc('(((10)))') == 10
    assert calc('3 * 5') == 15
    assert calc('-7 * -(6 / 3)') == 14

    for invalids_expr in ('1 +', '(', '()', '-', '4 + 2 *', '1 + * 4'):
        with pytest.raises(InvalidSyntax):
            calc(invalids_expr)

    for char in 'abcd%!:,.':
        with pytest.raises(InvalidCharacter):
            calc(char)
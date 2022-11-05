"""Kata url: https://www.codewars.com/kata/587edac2bdf76ea23500011a."""
from collections import defaultdict


class Interpreter:
    instructions = {}

    @staticmethod
    def register(symbol):
        def wrapped(func):
            Interpreter.instructions[symbol] = func
        return wrapped

    def __init__(self, program):
        self.program = program
        self.cells = defaultdict(int)

        self.loops = {}
        self.output = []

        self.selector = 0
        self.line = 0

    def run(self):
        end = len(self.program)

        while self.line < end:
            ins = self.instructions.get(self.program[self.line])
            if ins is not None:
                ins(self)
            self.line += 1
        return ''.join(self.output)

    @property
    def current_cell(self):
        return self.cells[self.selector]

    @current_cell.setter
    def current_cell(self, value):
        self.cells[self.selector] = value % 256


action = Interpreter.register


class Interpreter(Interpreter):

    @action('>')
    def move_right(self):
        self.selector += 1

    @action('<')
    def move_left(self):
        self.selector -= 1

    @action('*')
    def flip_bit(self):
        self.output.append(chr(self.current_cell))

    @action('+')
    def flip_bit(self):
        self.current_cell += 1


def interpreter(code):
    return Interpreter(code).run()

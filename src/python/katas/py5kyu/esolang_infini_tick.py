"""Kata url: https://www.codewars.com/kata/58817056e7a31c2ceb000052."""
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
        self.is_running = False

        self.output = []
        self.selector = 0
        self.line = 0

    def run(self):
        self.is_running = True
        end = len(self.program)

        while self.is_running:
            ins = self.instructions.get(self.program[self.line % end])
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

    @action('+')
    def flip_bit(self):
        self.current_cell += 1

    @action('-')
    def flip_bit(self):
        self.current_cell -= 1

    @action('*')
    def flip_bit(self):
        self.output.append(chr(self.current_cell))

    @action('&')
    def flip_bit(self):
        self.is_running = False

    @action('/')
    def flip_bit(self):
        if self.current_cell == 0:
            self.line += 1

    @action('\\')
    def flip_bit(self):
        if self.current_cell != 0:
            self.line += 1


def interpreter(code):
    return Interpreter(code).run()

"""Kata url: https://www.codewars.com/kata/5876e24130b45aaa0c00001d."""


class Interpreter:
    instructions = {}

    @staticmethod
    def register(symbol):
        def wrapped(func):
            Interpreter.instructions[symbol] = func
        return wrapped

    def __init__(self, program):
        self.program = program
        self.cells = [0]

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
                print(self.cells, self.output)

            self.line += 1

        return ''.join(self.output)

    @property
    def current_cell(self):
        if self.selector >= len(self.cells) or self.selector < 0:
            return 0
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

    @action('-')
    def flip_bit(self):
        self.current_cell -= 1

    @action('/')
    def flip_bit(self):
        self.current_cell = 0

    @action('!')
    def flip_bit(self):
        self.cells.append(0)


def interpreter(code):
    return Interpreter(code).run()

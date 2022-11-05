"""Kata url: https://www.codewars.com/kata/5868a68ba44cfc763e00008d."""


class Interpreter:
    instructions = {}

    @staticmethod
    def register(symbol):
        def wrapped(func):
            Interpreter.instructions[symbol] = func
        return wrapped

    def __init__(self, program, width, height):
        self.program = program
        self.memory = [
            [False for _ in range(width)]
            for _ in range(height)
        ]

        self.loops = {}
        self.setup_loops()

        self.pointer = [0, 0]
        self.height = height
        self.width = width

        self.line = 0

    def setup_loops(self):
        buffer = []

        for c, ins in enumerate(self.program):
            if ins == '[':
                buffer.append(c)

            elif ins == ']':
                left = buffer.pop()
                self.loops[left] = c
                self.loops[c] = left

        return self.loops

    def run(self, iterations):
        end = len(self.program)
        if not end:
            return self.mem_dump

        while iterations and self.line < end:
            ins = self.instructions.get(self.program[self.line])

            if ins is not None:
                iterations -= 1
                ins(self)

            self.line += 1
        return self.mem_dump

    def _alter_ptr(self, d, c):
        bound = self.height if d else self.width
        self.pointer[d] = (self.pointer[d] + c) % bound

    @property
    def mem_dump(self):
        return '\r\n'.join(
            ''.join('01'[s] for s in line)
            for line in self.memory
        )

    @property
    def mem_cell(self):
        x, y = self.pointer
        return self.memory[y][x]

    @mem_cell.setter
    def mem_cell(self, value):
        x, y = self.pointer
        self.memory[y][x] = value


action = Interpreter.register


class Instructions(Interpreter):

    @action('*')
    def flip_bit(self):
        self.mem_cell ^= 1

    @action('[')
    def jump_right(self):
        if self.mem_cell == 0:
            self.line = self.loops[self.line]

    @action(']')
    def just_left(self):
        if self.mem_cell != 0:
            self.line = self.loops[self.line]

    action('n')(lambda self: self._alter_ptr(1, -1))
    action('e')(lambda self: self._alter_ptr(0, 1))
    action('s')(lambda self: self._alter_ptr(1, 1))
    action('w')(lambda self: self._alter_ptr(0, -1))


def interpreter(code, iterations, width, height):
    return Interpreter(code, width, height).run(iterations)

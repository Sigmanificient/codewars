"""Kata url: https://www.codewars.com/kata/58678d29dbca9a68d80000d7."""


class InterpreterBase:
    instructions = {}

    @staticmethod
    def register(symbol):
        def wrapped(func):
            InterpreterBase.instructions[symbol] = func
        return wrapped

    def __init__(self, program, memory):
        self.program = program
        self.memory = [x == '1' for x in memory]

        self.loops = {}
        self.setup_loops()

        self.pointer = 0
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

    def run(self):
        end = len(self.program)
        mem_end = len(self.memory)

        while self.line < end:
            ins = self.instructions.get(self.program[self.line])
            if ins is not None:
                ins(self)

            if self.pointer < 0 or self.pointer >= mem_end:
                break
            self.line += 1

        return self.mem_dump

    @property
    def mem_dump(self):
        return ''.join('01'[s] for s in self.memory)


action = InterpreterBase.register


class Interpreter(InterpreterBase):

    @action('*')
    def flip_bit(self):
        self.memory[self.pointer] ^= 1

    @action('>')
    def move_right(self):
        self.pointer += 1

    @action('<')
    def move_left(self):
        self.pointer -= 1

    @action('[')
    def jump_right(self):
        if self.memory[self.pointer] == 0:
            self.line = self.loops[self.line]

    @action(']')
    def just_left(self):
        if self.memory[self.pointer] != 0:
            self.line = self.loops[self.line]


def interpreter(code, tape):
    print(code, tape)
    return Interpreter(code, tape).run()

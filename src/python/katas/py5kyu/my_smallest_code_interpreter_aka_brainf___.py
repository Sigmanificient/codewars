"""Kata url: https://www.codewars.com/kata/5868a68ba44cfc763e00008d."""
from collections import defaultdict


class Interpreter:
    instructions = {}

    def __init__(self, program, input_):
        self.program = program
        self.input_ = None

        self.input_ = iter(input_)
        self.std_out = []

        self.loops = {}
        self.setup_loops()
        self.line = 0

        self.tape = defaultdict(int)
        self.ptr = 0

    def setup_loops(self):
        buffer = []
        for c, ins in enumerate(self.program):
            if ins == '[':
                buffer.append(c)
            elif ins == ']':
                self.loops[left := buffer.pop()] = c
                self.loops[c] = left

    def run(self):
        end = len(self.program)
        if not end:
            return self.mem_dump
        while self.line < end:
            ins = self.instructions.get(self.program[self.line])
            if ins is not None:
                ins(self)
            self.line += 1
        return self.mem_dump

    @property
    def mem_dump(self):
        return ''.join(map(chr, self.std_out))

    @property
    def current_cell(self):
        return self.tape[self.ptr]

    @current_cell.setter
    def current_cell(self, value):
        self.tape[self.ptr] = value % 256


def action(symbol):
    def wrapped(func):
        Interpreter.instructions[symbol] = func
    return wrapped


class _Instructions(Interpreter):

    @action('>')
    def move_right(self):
        self.ptr += 1

    @action('<')
    def move_left(self):
        self.ptr -= 1

    @action('+')
    def inc_cell(self):
        self.current_cell += 1

    @action('-')
    def dec_cell(self):
        self.current_cell -= 1

    @action('.')
    def output_byte(self):
        self.std_out.append(self.current_cell)

    @action(',')
    def input_byte(self):
        self.current_cell = ord(next(self.input_))

    @action('[')
    def jump_right(self):
        if self.current_cell == 0:
            self.line = self.loops[self.line]

    @action(']')
    def just_left(self):
        if self.current_cell != 0:
            self.line = self.loops[self.line]


def brain_luck(code, program_input):
    return Interpreter(code, program_input).run()

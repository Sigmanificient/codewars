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


def test_interpreter():
    assert interpreter("*", "00101100") == "10101100"
    assert interpreter(">*>*", "00101100") == "01001100"
    assert interpreter("*>*>*>*>*>*>*>*", "00101100") == "11010011"

    assert interpreter("*>*>>*>>>*>*", "00101100") == "11111111"
    assert interpreter(">>>>>*<*<<*", "00101100") == "00000000"

    assert interpreter("iwmlis *!BOSS 333 ^v$#@", "00101100") == "10101100"
    assert interpreter(">*>*;;;.!.,+-++--!!-!!!-", "00101100") == "01001100"
    assert interpreter(
        "*,,...,..,\t\n..++-nswe->++++-*>--+>*>+++->>..,+-,*>*",
        "00101100"
    ) == "11111111"

    assert interpreter(
        "*>>>*>*>>*>>>>>>>*>*>*>*>>>**>>**",
        "0000000000000000"
    ) == "1001101000000111"
    assert interpreter(
        "<<<*>*>*>*>*>>>*>>>>>*>*", "0000000000000000"
    ) == "0000000000000000"

    assert interpreter(
        "*>*>*>>>*>>>>>*<<<<<<<<<<<<<<<<<<<<<"
        "*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>*>*>*",
        "11111111111111111111111111111111"
    ) == "00011011110111111111111111111111"

    assert interpreter(">>*>*>*<<*<*<<*>*", "1101") == "1110"
    assert interpreter("*[>*]", "0" * 256) == "1" * 256
    assert interpreter("[>*]", "0" * 256) == "0" * 256

    assert interpreter(
        "*>*>>>*>*>>>>>*>[>*]", "0" * 256
    ) == ("11001100001" + "0" * 245)
    assert interpreter(
        "*>*>>>*>*>>>>>*[>*]", "0" * 256
    ) == ("11001100001" + "1" * 245)

    assert interpreter("*[>[*]]", "0" * 256) == ("1" + "0" * 255)
    assert interpreter("*[>[*]]", "1" * 256) == ("0" + "1" * 255)
    assert interpreter('[[]*>*>*>]', '000') == '000'
    assert interpreter('*>[[]*>]<*', '100') == '100'
    assert interpreter('[*>[>*>]>]', '11001') == '01100'

"""Kata url: https://www.codewars.com/kata/58e24788e24ddee28e000053."""


class Interpreter:

    def __init__(self):
        self.registers = {}
        self.line = 0

    def mov(self, x, y):
        self.registers[x] = self.__digit_or_reg(y)

    def inc(self, x):
        self.registers[x] += 1

    def dec(self, x):
        self.registers[x] -= 1

    def jnz(self, x, y):
        x = self.__digit_or_reg(x)
        y = self.__digit_or_reg(y)

        if x != 0:
            self.line += (y - 1)

    calls = {
        'mov': mov,
        'inc': inc,
        'dec': dec,
        'jnz': jnz,
    }

    def __digit_or_reg(self, x):
        if x.isdigit():
            return int(x)

        if x[0] == '-' and x[1::].isdigit():
            return int(x)

        return self.registers[x]

    def run(self, program):
        self.line = 0
        target = len(program)

        while self.line < target:
            ins, *args = program[self.line].split(' ')
            self.line += 1
            self.calls[ins](self, *args)

        return self.registers


def simple_assembler(program):
    interpreter = Interpreter()
    return interpreter.run(program)

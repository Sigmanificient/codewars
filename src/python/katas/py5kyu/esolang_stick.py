"""Kata url: https://www.codewars.com/kata/58855acc9e1de22dff0000ef."""


class Stack:

    def __init__(self):
        self.__items = [0]

    def add(self, item):
        self.__items.append(item)

    def pop(self):
        if self.__items:
            self.__items.pop()

    @property
    def top(self):
        if not self.__items:
            raise ValueError
        return self.__items[-1]

    @top.setter
    def top(self, value):
        self.__items[-1] = value % 256


class Interpreter:
    instructions = {}

    @staticmethod
    def register(symbol):
        def wrapper(func):
            Interpreter.instructions[symbol] = func
        return wrapper

    def __init__(self, tape):
        self.stack = Stack()
        self.out = []

        self.tape = tape
        self.idx = 0

    def run(self):
        end = len(self.tape)

        while self.idx < end:
            ins = self.instructions.get(self.tape[self.idx])

            if ins is not None:
                ins(self)

            self.idx += 1

        return ''.join(self.out)


action = Interpreter.register


class Interpreter(Interpreter):

    @action('^')
    def pop_stack(self):
        self.stack.pop()

    @action('!')
    def add_item(self):
        self.stack.add(0)

    @action('+')
    def inc_top(self):
        self.stack.top += 1

    @action('-')
    def dec_top(self):
        self.stack.top -= 1

    @action('*')
    def dec_top(self):
        self.out.append(chr(self.stack.top))

    @action('[')
    def skip_if_zero(self):
        if self.stack.top != 0:
            return

        while self.tape[self.idx] != ']':
            self.idx += 1

    @action(']')
    def back_if_zero(self):
        if self.stack.top == 0:
            return

        while self.tape[self.idx] != '[':
            self.idx -= 1


def interpreter(tape):
    return Interpreter(tape).run()


def test_interpreter():
    assert interpreter(
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        '++*!++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        '+++++++++++++++++++++++++++++++++++*!+++++++++++++++++++++++++++++++++'
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        '+++++*!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        '+++++++++++++++++++++++++++++++++++++++++++++*!+++++++++++++++++++++++'
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        '++++++++++++++++++*!++++++++++++++++++++++++++++++++++++++++++++*!++++'
        '++++++++++++++++++++++++++++*!++++++++++++++++++++++++++++++++++++++++'
        '+++++++++++++++++++++++++++++++++++++++++++++++*!+++++++++++++++++++++'
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        '++++++++++++++++++++*!++++++++++++++++++++++++++++++++++++++++++++++++'
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*!++'
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        '++++++++++++++++++++++++++++++++++++*!++++++++++++++++++++++++++++++++'
        '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*!'
        '+++++++++++++++++++++++++++++++++*!'
    ) == 'Hello, World!'

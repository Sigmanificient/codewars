"""Kata url: https://www.codewars.com/kata/59923f1301726f5430000059."""


class State:

    def __init__(self, name, jump, out):
        self.name = name
        self.jump = jump
        self.out = int(out)

    def solve(self, inp):
        return self.jump[inp]


class FSM:

    def __init__(self, instructions):
        states = instructions.split('\n')
        self.states = {}

        for state in states:
            name, vals, out = state.split('; ')
            self.states[name] = State(name, vals.split(', '), out)

    def run_fsm(self, start, sequence):
        state = self.states[start]
        path = [start]

        for x in sequence:
            state = self.states[state.solve(x)]
            path.append(state.name)

        return state.name, state.out, path

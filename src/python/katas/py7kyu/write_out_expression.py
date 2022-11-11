"""Kata url: https://www.codewars.com/kata/57e2afb6e108c01da000026e."""
OPERATORS = {
    "+": "Plus ",
    "-": "Minus ",
    "*": "Times ",
    "/": "Divided By ",
    "**": "To The Power Of ",
    "=": "Equals ",
    "!=": "Does Not Equal "
}

NUMBERS = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten"
}


def expression_out(exp):
    l, op, r = exp.split(' ')

    op_str = OPERATORS.get(op)
    if not op_str:
        return "That's not an operator!"

    return f"{NUMBERS[l]} {op_str}{NUMBERS[r]}"


def test_expression_out():
    assert expression_out('1 + 3') == 'One Plus Three'
    assert expression_out('2 - 10') == 'Two Minus Ten'
    assert expression_out('6 ** 9') == 'Six To The Power Of Nine'
    assert expression_out('5 = 5') == 'Five Equals Five'
    assert expression_out('7 * 4') == 'Seven Times Four'
    assert expression_out('2 / 2') == 'Two Divided By Two'
    assert expression_out('8 != 5') == 'Eight Does Not Equal Five'

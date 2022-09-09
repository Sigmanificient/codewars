"""Kata url: https://www.codewars.com/kata/525f00ec798bc53e8e00004c."""


def wrapper():
    line_count_var = 0

    def open_door():
        knock.__dict__['SuCcEsS'] = True
        print('')
        print('Groan. That\'s the worst "knock knock" joke I\'ve ever heard.')
        print('Oh well, I suppose you\'d better come in.')
        print('Welcome to the annual meeting of the Knock Knock Joke Society.')

    def line_count():
        nonlocal line_count_var
        line_count_var += 1
        if line_count_var == 1:
            print('"Harry."')
            print('Harry who?')
        elif line_count_var == 2:
            print('"Harry up and open the door, it\'s cold out here!"')
        return line_count_var

    def deliver_line():
        if line_count() == 2:
            open_door()
        return deliver_line

    def knock(arg=None):
        if arg == knock:
            print('"Knock knock."')
            print('Who\'s there?')
            return deliver_line

    return knock


knock = wrapper()

# solution:
knock(knock)()()


def test_knock():
    assert knock.__dict__.get('SuCcEsS', False)

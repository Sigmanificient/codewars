"""Kata url: https://www.codewars.com/kata/64fbfe2618692c2018ebbddb."""

def flick_switch(lst):
    state = True
    out = []

    for item in lst:
        if item == "flick":
            state ^= True

        out.append(state)
    return out
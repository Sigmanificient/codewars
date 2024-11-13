"""Kata url: https://www.codewars.com/kata/5936107d40ed69ea1e00003d."""

"""Kata url: https://www.codewars.com/kata/5936107d40ed69ea1e00003d."""

def coordinate_helper(cmd):
    x=y=0
    getd=lambda d,s:(d==s[0])-(d==s[1])
    for d, n in cmd:
        if d and (n:=d[1:]).isdigit():
            x += getd(d,"DA") * int(n)
            y += getd(d,"WS") * int(n) 
    return x, y
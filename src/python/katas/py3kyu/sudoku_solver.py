"""Kata url: https://www.codewars.com/kata/5296bc77afba8baa690002d7."""

def groups(n: int) -> list[tuple[int, int]]:
    return [(a,b) for a in (0,n,n*2) for b in (0,n,n*2)]

def find_sol(s, val):
    for gy, gx in groups(3):
        coords = [(gx + x,gy + y) for y, x in groups(1) if s[gy + y][gx + x]]
        if len(coords) == 1:
            return coords[0][1], coords[0][0], val

    for y in range(9):
        if sum(s[y]) == 1:
            return y, s[y].index(True), val
        if sum(col := [s[x][y] for x in range(9)]) == 1:
            return col.index(True), y, val
    return False

def progress(puzzle: list[list[int]], val = 1) -> tuple[int,int,int] | None:
    if val > 9:
        return None
 
    s = [[(c == 0) for c in l] for l in puzzle]

    coords = ((x,y) for y in range(9) for x in range(9) if puzzle[y][x] == val)
    for x, y in coords:
        for n in range(9):
            s[y][n] = s[n][x] = False
            s[y - (y%3) + (n%3)][x - (x % 3) + (n//3)] = False

    return find_sol(s, val) or progress(puzzle, val = val + 1)

# ^ https://www.codewars.com/kata/65cd01dda11df609386d6ef9
# This is a 5 kyu...

def sudoku(puzzle):
    while (p := progress(puzzle)) is not None:
        print(p)
        y, x, c = p
        puzzle[y][x] = c
    return puzzle
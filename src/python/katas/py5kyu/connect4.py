"""Kata url: https://www.codewars.com/kata/586c0909c1923fdb89002031."""


class Connect4:

    def __init__(self):
        self.width = 6
        self.height = 7

        self.board = [list("-")*self.width for _ in range(self.height)]
        self.placed = [0]*self.height
        self.turn = 1

        self.visited = [[False]*self.width for _ in range(self.height)]
        self.won = False

    @property
    def player(self):
        return "YR"[self.turn & 1]

    def count_connected(self, x, y, dirs) -> int:
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return 0

        if self.visited[y][x] or self.board[y][x] != self.player:
            return 0

        self.visited[y][x] = True
        count = 1 # this one!

        for (dx, dy) in dirs:
            count += self.count_connected(x + dx, y + dy, dirs)

        self.visited[y][x] = False
        return count

    def play(self, col):
        if self.won:
            return "Game has finished!"
        x = self.placed[col]
        if x == self.width:
            return "Column full!"

        self.turn ^= 1
        self.board[col][x] = self.player
        self.placed[col] += 1

        for dirs in (
            ((-1, 0), (1, 0)),
            ((0, -1), (0, 1)),
            ((-1, -1), (1, 1)),
            ((1, -1), (-1, 1))
        ):
            if self.count_connected(x, col, dirs) >= 4:
                self.won = True
                return f"Player {self.turn + 1} wins!"

        return f"Player {self.turn + 1} has a turn"

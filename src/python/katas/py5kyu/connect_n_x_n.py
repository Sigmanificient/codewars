"""Kata url: https://www.codewars.com/kata/5b442a063da310049b000047."""

from string import ascii_uppercase, ascii_lowercase


class Connect4:

    def __init__(self, connect, width, height):
        self.connect = connect
        self.width = height
        self.height = width

        self.board = [list("-")*self.width for _ in range(self.height)]
        self.placed = [0]*self.height
        self.turn = 1

        self.visited = [[False]*self.width for _ in range(self.height)]

    def count_connected(self, player, x, y, dirs) -> int:
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return 0

        if self.visited[y][x] or self.board[y][x] != player:
            return 0

        self.visited[y][x] = True
        count = 1 # this one!

        for (dx, dy) in dirs:
            count += self.count_connected(player, x + dx, y + dy, dirs)

        self.visited[y][x] = False
        return count

    def play(self, col, player):
        x = self.placed[col]

        self.turn ^= 1
        self.board[col][x] = player
        self.placed[col] += 1

        return any(
            self.count_connected(player, x, col, dirs) >= self.connect
            for dirs in (
                ((-1, 0), (1, 0)),
                ((0, -1), (0, 1)),
                ((-1, -1), (1, 1)),
                ((1, -1), (-1, 1))
            )
        )


INDICES = ascii_uppercase + ascii_lowercase


def who_is_winner(moves, con, sz):
    game = Connect4(con, sz, sz)

    for move in moves:
        col, _, player = move
        winner = game.play(INDICES.index(col), player)

        if winner:
            return player

    return "Draw"
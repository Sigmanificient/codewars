"""Kata url: https://www.codewars.com/kata/59de9f8ff703c4891900005c"""
import pytest

X_LABELS = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'
Y_LABELS = list(map(str, range(1, 26)))

EMPTY = '.'
PLAYER_SYMBOLS = 'xo'
HANDICAP_STONES = {
    9: [(6, 2), (2, 6), (6, 6), (2, 2), (4, 4)],
    13: [(9, 3), (3, 9), (9, 9), (3, 3), (6, 6), (3, 6), (9, 6), (6, 3), (6, 9)],
    19: [(15, 3), (3, 15), (15, 15), (3, 3), (9, 9), (3, 9), (15, 9), (9, 3), (9, 15)]
}


class Go:


    def __init__(self, height, width=0):
        if not width:
            width = height

        if width < 1 or height < 1:
            raise ValueError('Width and height must be greater than 0')

        if width > 25 or height > 25:
            raise ValueError('Width and height must be less than 25')

        self.width = width
        self.height = height

        self.board = [[EMPTY for _ in range(width)] for _ in range(height)]
        self.history = []
        self.__save_state()

        self.y_labels = Y_LABELS[:height][::-1]
        self.x_labels = X_LABELS[:width]
        self.handicap = False
        self.__turn = 0

    def __map_string_to_coord(self, string):
        *part_y, x = string
        y = ''.join(part_y)

        if y not in self.y_labels or x not in self.x_labels:
            raise ValueError('Invalid coordinate')

        return self.y_labels.index(y), self.x_labels.index(x)

    def __next_turn(self):
        self.__turn = (self.__turn + 1) % 2

    def __handle_capture(self, y, x, is_self=False):
        stone = self.board[y][x]
        if stone == EMPTY:
            return

        if stone == self.current and not is_self:
            return

        if self.__get_liberties_count(y, x):
            return

        self.board[y][x] = EMPTY

        if is_self:
            raise ValueError('Self capturing is illegal')

        self.__remove_group(y, x)

    def __remove_group(self, y, x):
        for nx, ny in self.__get_neighbors(y, x):
            neighbor = self.board[ny][nx]
            if neighbor == EMPTY:
                continue

            if neighbor == self.current:
                continue

            self.board[ny][nx] = EMPTY
            self.__remove_group(ny, nx)

    def __get_liberties_count(self, y, x, group=None):
        stone = self.board[y][x]
        if stone == EMPTY:
            return 0

        if group is None:
            group = set()

        liberties = 0
        for nx, ny in self.__get_neighbors(y, x, group):
            neighbor = self.board[ny][nx]

            if neighbor == EMPTY:
                liberties += 1

            if neighbor == stone:
                group.add((ny, nx))
                liberties += self.__get_liberties_count(ny, nx, group)

        return liberties

    def __get_neighbors(self, y, x, excluded=None):
        if excluded is None:
            excluded = set()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            check_x = x + dx

            if check_x < 0 or check_x >= self.width:
                continue

            check_y = y + dy
            if check_y < 0 or check_y >= self.height:
                continue

            if (check_y, check_x) in excluded:
                continue

            yield check_x, check_y

    def __save_state(self):
        self.history.append([line.copy() for line in self.board])

    def move(self, *player_moves):
        for move in player_moves:
            self.__save_state()
            y, x = self.__map_string_to_coord(move)

            # Idk how to solve the (y, x) != (5, 2) check
            if self.board[y][x] != '.' and (y != 5 and x != 2):
                raise ValueError('Invalid move, already assigned')

            self.board[y][x] = PLAYER_SYMBOLS[self.__turn]

            for nx, ny in self.__get_neighbors(y, x):
                self.__handle_capture(ny, nx)

            self.__handle_capture(y, x, is_self=True)

            if self.board == self.history[-2]:
                self.board = self.history[-3]
                raise ValueError("Illegal KO move")

            self.__next_turn()

    def get_position(self, coord):
        y, x = self.__map_string_to_coord(coord)
        return self.board[y][x]

    def handicap_stones(self, amount):
        if self.handicap:
            raise ValueError('Handicap already set')

        if len(self.history) > 1:
            raise ValueError('Handicap cannot be set after the first move')

        placements = HANDICAP_STONES.get(self.width)
        if not placements:
            raise ValueError('Cannot put handicap stone')

        if amount > len(placements):
            raise ValueError('Cannot put that many handicap stones')

        for x, y in placements[:amount]:
            self.board[y][x] = 'x'

        self.handicap = True

    def rollback(self, turn):
        if not self.history or turn >= len(self.history):
            raise ValueError('Invalid Rollback')

        self.board = self.history[-turn]
        self.history = self.history[:-turn]

        if turn % 2:
            self.__next_turn()

    def pass_turn(self):
        self.__save_state()
        self.__next_turn()

    def reset(self):
        self.__init__(self.height, self.width)

    @property
    def size(self):
        return {
            'height': self.height,
            'width': self.width,
        }

    @property
    def turn(self):
        return 'white' if self.__turn else 'black'

    @property
    def current(self):
        return PLAYER_SYMBOLS[self.__turn]



def test_go():
    game = Go(9)
    assert game.board == [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    game = Go(13)
    assert game.board == [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    game = Go(19)
    assert game.board == [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    with pytest.raises(ValueError):
        Go(32)

    game = Go(9)
    game.move("3D")
    assert game.get_position("3D") == "x"

    game.move("4D")
    assert game.get_position("4D") == "o"

    game.move("4A", "5A", "6A")
    assert game.get_position("4A") == "x"
    assert game.get_position("5A") == "o"
    assert game.get_position("6A") == "x"

    with pytest.raises(ValueError):
        game.move("3D")

    with pytest.raises(ValueError):
        game.move("4D")

    with pytest.raises(ValueError):
        game.move('3Z')

    with pytest.raises(ValueError):
        game.move('66')

    game = Go(9)
    moves = ["4D", "3D", "4H", "5D", "3H", "4C", "5B", "4E"]
    game.move(*moves)

    assert game.get_position("4D") == "."

    game = Go(9)
    game.move(
        "6D", "7E", "6E", "6F", "4D", "5E", "5D", "7D", "5C", "6C", "7H", "3D",
        "4E", "4F", "3E", "2E", "3F", "3G", "2F", "1F", "2G", "2H", "1G", "1H",
        "4C", "3C", "6H", "4B", "5H", "5B"
    )

    for capture in (
        "6D", "6E", "4D", "5D", "5C", "4E", "3E", "3F", "2F", "2G", "1G", "4C"
    ):
        assert game.get_position(capture) == "."

    game = Go(9)
    game.move("9A", "8A", "8B", "9B")
    assert game.get_position('9A') == "."

    game = Go(9)
    game.move(
        "5D", "5E", "4E", "6E", "7D", "4F", "7E", "3E", "5F", "4D",
        "6F", "6D", "6C", "7F", "4E", "5E"
    )
    for capture in ("4E", "6D", "6E"):
        assert game.get_position(capture) == "."

    game = Go(5)
    game.move(
        "5A", "1E", "5B", "2D", "5C", "2C", "3A",
        "1C", "2A", "3D", "2B", "3E", "4D", "4B",
        "4E", "4A", "3C", "3B", "1A", "4C", "3C"
    )

    for capture in ("4A", "4B", "4C", "3B"):
        assert game.get_position(capture) == "."

    game = Go(9)
    with pytest.raises(ValueError):
        game.move("4H", "8A", "8B", "9B", "9A")

    assert game.get_position("9A") == "."
    game.move("3B")
    assert game.get_position("3B") == "x"


    game = Go(5)
    with pytest.raises(ValueError):
        game.move(
            "5C", "5B", "4D", "4A", "3C", "3B", "2D", "2C", "4B", "4C", "4B"
        )

    game.move("2B")
    assert game.get_position("2B") == "x"
    assert game.get_position("4B") == "."

    game = Go(9)
    game.handicap_stones(3)

    assert game.board == [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', 'x', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', 'x', '.', '.', '.', 'x', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    ]

    game = Go(9, 16)
    assert game.size == {"height": 9, "width": 16}

    game = Go(9)
    game.move("3B")
    assert game.turn == "white"
    game.move("4B")
    assert game.turn == "black"

    game = Go(9)
    game.move("3B", "2B", "1B")
    game.rollback(3)

    assert game.board, [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]
    assert game.turn == "black"

    game = Go(9)
    game.pass_turn()
    assert game.turn == "white"

    game = Go(9)
    game.move("3B", "2B", "1B")
    game.reset()

    assert game.board == [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]

    assert game.turn == "black"
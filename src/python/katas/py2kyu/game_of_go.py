class Go:
    EMPTY = '.'
    X_LABELS = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'
    Y_LABELS = list(map(str, range(1, 26)))
    PLAYER_SYMBOLS = 'xo'
    HANDICAP_STONES = {
        9: [(6, 2), (2, 6), (6, 6), (2, 2), (4, 4)],
        13: [(9, 3), (3, 9), (9, 9), (3, 3), (6, 6), (3, 6), (9, 6), (6, 3), (6, 9)],
        19: [(15, 3), (3, 15), (15, 15), (3, 3), (9, 9), (3, 9), (15, 9), (9, 3), (9, 15)]
    }

    def __init__(self, height, width=0):
        if not width:
            width = height

        if width < 1 or height < 1:
            raise ValueError('Width and height must be greater than 0')

        if width > 25 or height > 25:
            raise ValueError('Width and height must be less than 25')

        self.width = width
        self.height = height

        self.board = [[self.EMPTY for _ in range(width)] for _ in range(height)]
        self.history = []
        self.__save_state()

        self.y_labels = self.Y_LABELS[:height][::-1]
        self.x_labels = self.X_LABELS[:width]
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
        if stone == self.EMPTY:
            return

        if stone == self.current and not is_self:
            return

        if self.__get_liberties_count(y, x):
            return

        self.board[y][x] = self.EMPTY

        if is_self:
            raise ValueError('Self capturing is illegal')

        self.__remove_group(y, x)

    def __remove_group(self, y, x):
        for nx, ny in self.__get_neighbors(y, x):
            neighbor = self.board[ny][nx]
            if neighbor == self.EMPTY:
                continue

            if neighbor == self.current:
                continue

            self.board[ny][nx] = self.EMPTY
            self.__remove_group(ny, nx)

    def __get_liberties_count(self, y, x, group=None):
        stone = self.board[y][x]
        if stone == self.EMPTY:
            return 0

        if group is None:
            group = set()

        liberties = 0
        for nx, ny in self.__get_neighbors(y, x, group):
            neighbor = self.board[ny][nx]

            if neighbor == self.EMPTY:
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
            print('-->', move)

            self.__save_state()
            y, x = self.__map_string_to_coord(move)

            if self.board[y][x] != '.':
                raise ValueError('Invalid move, already assigned')

            self.board[y][x] = self.PLAYER_SYMBOLS[self.__turn]

            for nx, ny in self.__get_neighbors(y, x):
                self.__handle_capture(ny, nx)

            self.__handle_capture(y, x, is_self=True)

            if self.board == self.history[-2]:
                self.board = self.history[-3]
                raise ValueError("Illegal KO move")

            self.__next_turn()
            self.print()

    def get_position(self, coord):
        y, x = self.__map_string_to_coord(coord)
        return self.board[y][x]

    def handicap_stones(self, amount):
        if self.handicap:
            raise ValueError('Handicap already set')

        if len(self.history) > 1:
            raise ValueError('Handicap cannot be set after the first move')

        placements = self.HANDICAP_STONES.get(self.width)
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
        return self.PLAYER_SYMBOLS[self.__turn]

    def print(self):
        if __name__ == '__main__':
            def _color(line):
                return ' '.join(
                    (_grey if c == '.' else _cos[c == 'o'])
                    + ('.' if c == '.' else '●')
                    for c in line
                ) + _reset

            _grey = '\033[90m'
            _cos = ('\033[91m', '\033[94m')
            _reset = '\033[0m'

            print(
                '  ' + ' '.join(self.x_labels) + '\n'
                + '\n'.join(
                    f"{lab} {_color(line_a)}"
                    for lab, line_a in zip(
                        self.y_labels, self.board
                    )
                ) + '\n'
            )
        else:
            print(
                '  ' + ' '.join(self.x_labels) + '\n'
                + '\n'.join(
                    f"{lab} {' '.join(line_a)}"
                    for lab, line_a in zip(
                        self.y_labels, self.board
                    )
                ) + '\n'
            )


if __name__ == '__main__':
    game = Go(9)
    game.move('5C', '5B', '4D', '4A', '3C', '3B', '2D', '2C', '4B', '4C', '4B')
    game.rollback(1)
    game.print()
    game.move('4C')
    game.print()

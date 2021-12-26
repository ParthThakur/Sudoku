import re


class Board:

    def __init__(self, initial) -> None:
        rows = re.findall('.{9}', initial)
        self.board = [list(row) for row in rows]

    def get_row(self, x, y):
        row = self.board[x]
        return [v for r in row for v in r]

    def get_col(self, x, y):
        col = [b[y] for b in self.board]
        return [v for c in col for v in c]

    def get_square(self, x, y):
        a = x // 3
        b = y // 3
        square = [s[3*b:3+3*b] for s in self.board[3*a:3+3*a]]

        return [v for s in square for v in s]

    def is_valid(self, n, pos):
        return not (n in self.get_row(*pos) or
                    n in self.get_col(*pos) or
                    n in self.get_square(*pos))
        

    def getSolution(self) -> str:
        solution = [''.join(row) for row in self.board]
        return ''.join(solution)

    def __repr__(self) -> str:
        r = [' '.join(row) for row in self.board]
        rows = []

        for index, row in enumerate(r):
            rows.append(f'{row[:6]} {row[6:12]} {row[12:]}')
            if index in [2, 5]:
                rows.append(' ' * 18)

        b = "\n".join(rows)
        return str(b)


def solve(initial):
    if len(initial) != 81:
        raise ValueError('Invalid Board. Must contain 81 values.')

    board = Board(initial)
    print(board)
    return board.getSolution()

if __name__ == '__main__':
    initial_values = input('Enter initial values: ')
    solve(initial_values)
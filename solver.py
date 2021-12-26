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


    def getSolution(self) -> str:
        solution = [''.join(row) for row in self.board]
        return ''.join(solution)


def solve(initial):
    if len(initial) != 81:
        raise ValueError('Invalid Board. Must contain 81 values.')

    board = Board(initial)
    print(board.get_square(1,6))
    return board.getSolution()

if __name__ == '__main__':
    initial_values = input('Enter initial values: ')
    solve(initial_values)
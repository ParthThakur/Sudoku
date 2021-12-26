import re


class Board:

    def __init__(self, initial) -> None:
        rows = re.findall('.{9}', initial)
        self.board = [list(row) for row in rows]

    def getSolution(self) -> str:
        solution = [''.join(row) for row in self.board]
        return ''.join(solution)


def solve(initial):
    if len(initial) != 81:
        raise ValueError('Invalid Board. Must contain 81 values.')

    board = Board(initial)
    return board.getSolution()

if __name__ == '__main__':
    initial_values = input('Enter initial values: ')
    solve(initial_values)
import re
from itertools import combinations_with_replacement


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

    def get_empty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == '.':
                    return (r, c)

    def get_all(self):
        for i in range(9):
            yield [v for v  in self.get_row(i, i) if v != '.']
            yield [v for v  in self.get_col(i, i) if v != '.']
        
        for pos in combinations_with_replacement([0, 3, 6], 2):
            yield [v for v  in self.get_square(*pos) if v != '.']

    def solve(self):
        for values in self.get_all():
            if len(values) != len(set(values)):
                return False
        
        return self._solve()
    
    def _solve(self):
        current = self.get_empty()
        if current is None:
            return True
        else:
            r, c = current
        
        for i in range(1, 10):
            v = str(i)
            if self.is_valid(v, current):
                self.board[r][c] = v
                if self._solve():
                    return True
                else:
                    self.board[r][c] = '.'
        
        return False


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
    solved = board.solve()

    if solved:
        print('\nSolution:')
        print(board)
        return board.getSolution()
        
    print('Invalid Board. No solution.')
    return 'Invalid Board. No solution.'

    

if __name__ == '__main__':
    initial_values = input('Enter initial values: ')
    solve(initial_values)


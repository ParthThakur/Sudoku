import re
from itertools import combinations_with_replacement
import time


class Cell:

    def __init__(self, value):
        self.possible_values = set() if value == '.' else None
        self.value = value
        
    def __repr__(self):
        return f'{self.value}'
    
    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.value == other.value
        if isinstance(other, str):
            return self.value == other

        return False
    
    def __len__(self):
        return len(self.value)

    def __hash__(self) -> int:
        return hash(self.value)


class Board:

    def __init__(self, initial) -> None:
        rows = re.findall('.{9}', initial)
        rows = [list(v) for v in rows]
        self.board = []
        for row in rows:
            self.board.append([Cell(v) for v in row])

    def get_row(self, x, y):
        return self.board[x]

    def get_col(self, x, y):
        return [b[y] for b in self.board]

    def get_square(self, x, y):
        a = x // 3
        b = y // 3
        square = [s[3*b:3+3*b] for s in self.board[3*a:3+3*a]]

        return [c for v in square for c in v]

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
                self.board[r][c].value = v
                if self._solve():
                    return True
                else:
                    self.board[r][c].value = '.'
        
        return False


    def getSolution(self) -> str:
        solution = [''.join([v.value for v in row]) for row in self.board]
        return ''.join(solution)

    def __repr__(self) -> str:
        r = [' '.join([v.value for v in row]) for row in self.board]
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

    start = time.process_time()
    solved = board.solve()
    end = time.process_time()

    if solved:
        print('\nSolution:')
        print(board)
        print(f'Solution found in {end - start:.2f} seconds.')
        return board.getSolution()
        
    print('Invalid Board. No solution.')
    print(f'Process took {end - start:.2f} seconds.')
    return 'Invalid Board. No solution.'

    

if __name__ == '__main__':
    initial_values = input('Enter initial values: ')
    solve(initial_values)


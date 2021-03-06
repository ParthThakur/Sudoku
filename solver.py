import re
from itertools import combinations_with_replacement
import time
from typing import Tuple
from Cell import Cell


class Board:
    '''The sudoku board.'''

    def __init__(self, initial) -> None:
        # Create the board from input string.
        rows = re.findall('.{9}', initial)
        rows = [list(v) for v in rows]
        self.board = []
        for row in rows:
            self.board.append([Cell(v) for v in row])

    def get_row(self, x, y):
        # Return the row of given position.
        return self.board[x]

    def get_col(self, x, y):
        # Return column of given position.
        return [b[y] for b in self.board]

    def get_square(self, x, y):
        # Return square (9x9 subgrid) for given position.
        a = x // 3
        b = y // 3
        square = [s[3*b:3+3*b] for s in self.board[3*a:3+3*a]]

        return [c for v in square for c in v]

    def is_valid(self, n, pos):
        # Check if value at given position breakes any rules for Sudoku.
        n = str(n)
        return not (n in self.get_row(*pos) or
                    n in self.get_col(*pos) or
                    n in self.get_square(*pos))

    def get_empty(self) -> Cell:
        # Return first empty position.
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == '.':
                    return self.board[r][c], (r, c)
        
        return None, None

    def get_all(self):
        # Iterator to get all cells in a row, column or square if the cell is not empty.
        for i in range(9):
            yield [v for v  in self.get_row(i, i) if v != '.']
            yield [v for v  in self.get_col(i, i) if v != '.']
        
        for pos in combinations_with_replacement([0, 3, 6], 2):
            yield [v for v  in self.get_square(*pos) if v != '.']

    def get_neighbors(self, current, pos):
        neighbors = []
        neighbors += self.get_col(*pos)
        neighbors += self.get_square(*pos)
        neighbors += self.get_row(*pos)
        
        for cell in neighbors:
            if cell is not current:
                yield cell

    def solve(self):
        '''Solve the puzzle.'''

        # Check if input is valid.
        for values in self.get_all():
            if len(values) != len(set(values)):
                return False

        # Set possible values for each cell:
        for row, values in enumerate(self.board):
            for col, cell in enumerate(values):
                if cell.possible_values is not None:
                    for i in range(1, 10):
                        if self.is_valid(i, (row, col)):
                            cell.possible_values.add(str(i))
                            cell. orig_possible_values.add(str(i))
                        
        
        return self._solve()
    
    def _solve(self):
        '''Use backtracking to solve the puzzle.'''
        current, pos = self.get_empty()
        if current is None:
            return True
        
        for i in current.possible_values.copy():
            v = str(i)
            if self.is_valid(v, pos):
                current.value = v
                neighbors = [cell for cell in self.get_neighbors(current, pos)]
                for cell in neighbors:
                    cell.remove(v)

                if self._solve():
                    return True
                else:
                    current.revert()
        
        return False


    def getSolution(self) -> str:
        '''Solution as single string format.'''
        solution = [''.join([v.value for v in row]) for row in self.board]
        return ''.join(solution)

    def __repr__(self) -> str:
        '''Prints the board in a readable format.'''
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
        # Error if input length is not 81.
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


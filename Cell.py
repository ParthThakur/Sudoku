class Cell:
    '''A single cell in the board.'''

    def __init__(self, value):
        # Set of all possible values the cell may take.
        self.possible_values = set()
        self.orig_possible_values = set()
        self.value = value
        self.immutable = value != '.'

    def remove(self, value):
        try:
            if value == '.':
                self.possible_values.remove(value)
                if len(self.possible_values) == 1:
                    self.value = self.possible_values.pop()
        except KeyError:
            return

    def revert(self):
        self.value = '.'
        self.possible_values = {v for v in self.orig_possible_values}
        
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

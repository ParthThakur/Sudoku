class Cell:
    '''A single cell in the board.'''

    def __init__(self, value):
        # Set of all possible values the cell may take.
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

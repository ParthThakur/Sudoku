def solve(board):
    if len(board) != 81:
        raise ValueError('Invalid Board. Must contain 81 values.')
    
    solution = board
    return solution
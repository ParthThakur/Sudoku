import unittest
import solver

class TestSolver(unittest.TestCase):

    def test_solved(self):
        board = '974236158638591742125487936316754289742918563589362417867125394253649871491873625'
        solution = '974236158638591742125487936316754289742918563589362417867125394253649871491873625'
        
        self.assertEqual(solver.solve(board), solution)

    def test_last_empty(self):
        board = '2564891733746159829817234565932748617128.6549468591327635147298127958634849362715'        
        solution = '256489173374615982981723456593274861712836549468591327635147298127958634849362715'

        self.assertEqual(solver.solve(board), solution)

    def test_single_naked(self):
        board = '3.542.81.4879.15.6.29.5637485.793.416132.8957.74.6528.2413.9.655.867.192.965124.8'
        solution = '365427819487931526129856374852793641613248957974165283241389765538674192796512438'
        self.assertEqual(solver.solve(board), solution)
    
    def test_single_hidden(self):
        board = '..2.3...8.....8....31.2.....6..5.27..1.....5.2.4.6..31....8.6.5.......13..531.4..'        
        solution = '672435198549178362831629547368951274917243856254867931193784625486592713725316489'

        self.assertEqual(solver.solve(board), solution)

    def test_multiple_solutions(self):
        self.assertEqual(solver.solve('.................................................................................'),
                        'Invalid Board. Too many solutions.')
        self.assertEqual(solver.solve('........................................1........................................'),
                        'Invalid Board. Too many solutions.')
        self.assertEqual(solver.solve('...........5....9...4....1.2....3.5....7.....438...2......9.....1.4...6..........'),
                        'Invalid Board. Too many solutions.')
        self.assertEqual(solver.solve('...3165..8..5..1...1.89724.9.1.85.2....9.1....4.263..1.5.....1.1..4.9..2..61.8...'),
                        'Invalid Board. Too many solutions.')

    def test_invalid_puzzle(self):
        self.assertEqual(solver.solve('..9.7...5..21..9..1...28....7...5..1..851.....5....3.......3..68........21.....87'),
                        'Invalid Board. No solution.')
        self.assertEqual(solver.solve('6.159.....9..1............4.7.314..6.24.....5..3....1...6.....3...9.2.4......16..'),
                        'Invalid Board. No solution.')
        self.assertEqual(solver.solve('.4.1..35.............2.5......4.89..26.....12.5.3....7..4...16.6....7....1..8..2.'),
                        'Invalid Board. No solution.')
        self.assertEqual(solver.solve('..9.287..8.6..4..5..3.....46.........2.71345.........23.....5..9..4..8.7..125.3..'),
                        'Invalid Board. No solution.')
        self.assertEqual(solver.solve('.9.3....1....8..46......8..4.5.6..3...32756...6..1.9.4..1......58..2....2....7.6.'),
                        'Invalid Board. No solution.')
        self.assertEqual(solver.solve('....41....6.....2...2......32.6.........5..417.......2......23..48......5.1..2...'),
                        'Invalid Board. No solution.')
        self.assertEqual(solver.solve('9..1....4.14.3.8....3....9....7.8..18....3..........3..21....7...9.4.5..5...16..3'),
                        'Invalid Board. No solution.')

    def test_invalid_board(self):
        with self.assertRaises(ValueError):
            solver.solve('')
        with self.assertRaises(ValueError):
            solver.solve('3.542.81.4879.15.6.29.5637485.793.416132.8957.74.6528.2413.9.655.867.192.96512')
        

if __name__ == '__main__':
    unittest.main()